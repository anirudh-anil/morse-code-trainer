# MORSE CODE WORD TRAINER

This is a simple program that can be used to train recieving morse code using words from a given wordlist file.
The program expects user to have some kind of experience recieving morse code and is origanally intended to make the user faster when recognizing words by hearing morse code

> [!Warning]
> Before you run the program, or the test, you should install `PortAudio` on your system

## Installing PortAudio

In this section I'm giving the usual commands that can be used to install PortAudio on your system. Please note that this dont cover every single distros/OSes out there but I have included some common ones.

> [!Note]
> User is recommended to visit [PortAudio's Website](https://portaudio.com/)

### Fedora or Fedora Based Systems

```
sudo dnf install portaudio portaudio-devel
```

### Debian or Debian Based Systems

```
sudo apt install portaudio19-dev
```

### macOS

first install [Homebrew](https://brew.sh)
```
brew install portaudio
```

### Windows
PortAudio should be installed by default when you run
```
pip install sounddevice
```

## Program Usage

Video Demo: https://youtu.be/ullwVs9Ib5o


[![Video Title](https://img.youtube.com/vi/ullwVs9Ib5o/0.jpg)](https://www.youtube.com/watch?v=ullwVs9Ib5o)




```
usage: project.py [-h] [-c ] [-w ] [-f ] [-d ] [-v ] [-S ] [-D]

Simple Morse Code Word Trainer

options:
  -h, --help       show this help message and exit
  -c, --count      Number of Words
  -w, --wordlist   Wordlist file to use
  -f, --freq       Frequency in Hz
  -d, --dotlen     Dot character lenght in ms
  -v, --volume     Volume between 0 and 100
  -S, --spacing    Spacing between words in ms
  -D, --debug
```
### count

The flag is used to specify how many words should the program play to the user. Words are chosen randomly from the wordlist file.
- Expects: integer (>0)
- Default Value: 1

### wordlist

Used to specify the wordlist to use. If unspecified or specified file does not exist, program looks for `wordlist.txt` in its current working directory and uses it, if found. If the file is not found, the program downloads [a wordlist](https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt) and then uses it.
- Expects: text file
- Default Value: wordlist.txt

### frequency

Used to specify the frequency of the sound output in Hz
- Expects: integer
- Default Value: 440

### dotlength

Used to specify the "dot" character length in milliseconds. The "dash" character length will be thrice that of the dot character.
- Expects: integer
- Default Value: 100

### Volume

Sets the program output volume (Not the system volume)
- Expects: integer between 0 and 100
- Default Value: 100

### Spacing

Sets the word spacing in milliseconds
- Expects: integer
- Default Value: 1000

### Debug

Enables the debug option, ie prints a python `list` of the words that will be converted to morse code audio
