import requests
import random, argparse, os, sys, time, multiprocessing
import numpy as np

# Please install PortAudio on your system, or the sound production wont work
try:
    import sounddevice as sd
except OSError as err:
    sys.exit(err)


sample_rate = 44100
freq_hz = 440.0
duration_ms = 100
volume_level = 100
spacing = 1000




morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}


def main():
    parser = argparse.ArgumentParser(description="Simple Morse Code Word Trainer")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of Words", metavar="")
    parser.add_argument("-w", "--wordlist", type=str, default="wordlist.txt",metavar="" ,help="Wordlist file to use")
    parser.add_argument("-f", "--freq", type=int, default=440, help="Frequency in Hz", metavar="")
    parser.add_argument("-d", "--dotlen", type=int, help="Dot character lenght in ms", default=100, metavar="")
    parser.add_argument("-v", "--volume", type=int, help="Volume between 0 and 100", default=100, metavar="")
    parser.add_argument("-S", "--spacing", help="Spacing between words in ms", default=1000, type=int, metavar="")
    parser.add_argument("-D", "--debug", action='store_true', default=False, required=False)
    args = parser.parse_args()
    
    global freq_hz
    if int(args.freq) <= 0:
        sys.exit("Invalid frequency")
    freq_hz = args.freq

    
    global duration_ms
    if int(args.dotlen) <= 0:
        sys.exit("Invalid dot character speed") 
    duration_ms = args.dotlen

    global volume_level
    if not (0<= int(args.volume) <= 100):
        sys.exit("Invalid volume")
    volume_level = args.volume

    if int(args.count) <= 0:
        sys.exit("Count should be greater than or equal to 1")
    
    if int(args.spacing) < 0:
        sys.exit("Invalid spacing")
    global spacing
    spacing = args.spacing

    
    wrd = wordlist(args.wordlist)
    words = getwords(wrd, args.count)
    if args.debug:
        print(words)
    
    soundproc = multiprocessing.Process(target=sound, args=words)
    soundproc.start()
    
    
    usrinp = input("> ").strip().upper().split(" ")
    print(f"Provided: {" ".join(words)}")
    print(f"Entered: {" ".join(usrinp)}")
    soundproc.terminate()
    print()
    print(f"Your score is {score(words, usrinp)}/{len(words)}")
    

def sound(*words):
    for wrds in words:
        for stuff in convert(wrds):
            for characters in stuff:
                match characters:
                    case ".":
                        each_sample_number = np.arange((duration_ms/1000) * sample_rate)
                        waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sample_rate)
                        sd.play(waveform * (volume_level/100), sample_rate)
                        time.sleep(((3 * duration_ms)/2000))
                    case "-":
                        each_sample_number = np.arange((duration_ms/1000) * 3 * sample_rate)
                        waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sample_rate)
                        sd.play(waveform * (volume_level/100), sample_rate)
                        time.sleep((duration_ms/1000) * 3)
            time.sleep((duration_ms/1000) * 3)
        time.sleep(spacing/1000)
    return 0
    
    

def score(a, b):
    if len(b) > len(a):
        sys.exit("Check input")
    usrscore = 0
    for i, word in enumerate(b):
        if a[i] == word:
            usrscore += 1
        else:
            pass
    return usrscore



def convert(_word):
    if _word.isalpha() == False:
        raise ValueError("Wordlist error, contains non alphabet characters")
    for _char in _word.upper():
        yield morse[_char]


def getwords(_file, num):
    with open(_file, "r") as file:
        wrds = list(word.strip().upper() for word in file)
    return random.choices(wrds, k=int(num))

def wordlist(w):
    if os.path.exists(w):
        return str(w)
    elif os.path.exists("wordlist.txt"):
        print(f"{w} does not exist, Using existing wordlist.txt")
        return "wordlist.txt"
    else:
        print(f"neither {w} nor wordlist.txt exist, downloading new wordlist")
        web = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt")
        with open("wordlist.txt", "w") as dictfile:
            dictfile.write(web.text)
        return "wordlist.txt"


if __name__ == "__main__":
    main()
    
