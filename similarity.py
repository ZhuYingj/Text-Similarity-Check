'''
This mini project compares the words of 2 texts to see the similarity between them.
It only takes as parameters 2 strings with the suffixe .txt.
'''

import string
import re
from stop_words import stop_words

'''
This function cleans the text by removing the punctuations and useless/support words
that have no real meaning. For example : I, am, etc.

Takes a str for the file name as an argument ( finishing by .txt )
'''

def clean_text(filename: str) -> set:
    with open(filename, encoding="utf-8") as f:
        set_words = set()
        pattern = f"[{re.escape(string.punctuation)}]"
        for line in f:
            line = line.lower().strip()
            line = re.sub(pattern, '', line)
            set_words.update(line.split())
    return remove_support_words(set_words)

'''
Removes support words from a set

Takes a set of words as argument
'''

def remove_support_words(setWords: set) -> set:
    return setWords.difference(stop_words)

'''
Checks the intersection and union to calculate the similarity between the texts by dividing the lenght
of the intersection of the two sets by the union.

Takes two files names (str) as arguments
'''

def check_text_similarity(firstFile:str, secondFile:str) -> None:
    firstSet = clean_text(firstFile)
    secondSet = clean_text(secondFile)

    intersection = len(firstSet.intersection(secondSet))
    union = len(firstSet.union(secondSet))

    nameFirstFile, nameSecondFile = firstFile.removesuffix(".txt"), secondFile.removesuffix(".txt")
    print(f"The similarity between the texts {nameFirstFile} and {nameSecondFile} is {((intersection / union) * 100):.2f} %")

check_text_similarity('obama_speech.txt', 'donald_speech.txt')