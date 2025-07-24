import pytest , os, random
from project import convert 
from project import wordlist
from project import getwords
from project import score

testwords = ["a", "as", "cat", "crow", "woman", "select"]
with open("test_wordlist.txt", "w") as _wordlist:
    for word in testwords[:-1]:
        _wordlist.write(f"{word}\n")
    _wordlist.write(testwords[-1])

def test_wordlist():
    assert wordlist("test_wordlist.txt") == "test_wordlist.txt"
    try:
        os.remove("wordlist.txt")
    except FileNotFoundError():
        pass
    assert wordlist("wordlist.txt") == "wordlist.txt"
    assert wordlist("sgergbskdbvsovsbv") == "wordlist.txt"

def test_getwords():
    random.seed(0)
    assert getwords("test_wordlist.txt", 1) == ["SELECT"]
    assert getwords("test_wordlist.txt", 2) == ["WOMAN", "CAT"]
    os.remove("test_wordlist.txt")
    

def test_score():
    l1 = ["hi", "hello", "sup"]
    l2 = ["hi", "morning", "sup"]
    assert score(l1, l2) == 2

def test_convert():
    with pytest.raises(ValueError):
        for _ in convert("-=23"):
            print(_)
    testlist = []
    for t in convert("aBcD"):
        testlist.append(t)
    assert ".- -... -.-. -.." == " ".join(testlist)

