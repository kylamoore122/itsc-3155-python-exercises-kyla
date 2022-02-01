# Author: Kyla Moore
# Created: 01/28/2022
# Course: ITSC 3155

def countLetters(string):
    litter = {}

    for ch in string:
        if ch in litter:
            litter[ch] += 1
        else:
            litter[ch] = 1

    return litter

phrase = ""
letterDict = {}

phrase = input("Enter a phrase: ")

letterDict = countLetters(phrase)

print("Letter List: " + str(letterDict))
