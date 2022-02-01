# Author: Kyla Moore
# Created: 01/28/2022
# Course: ITSC 3155

def combineDictionaries(dict1, dict2):
    newDict = dict1

    for ch in dict1:
        if ch in dict2 and ch in newDict:
            newDict[ch] += dict2[ch]
    
    for ch in dict2:
        if ch in dict2 and not(ch in newDict):
            newDict[ch] = dict2[ch]

    return newDict

myDict1 = {}
#myDict1 = {'a':5, 'b':12, 'c':3, 'd':9}
myDict2 = {}
#myDict2 = {'b':4, 'c':9, 'd':10, 'e':16}
combinedDict = {}
key = ''
value = 0

# Get input for myDict1
for i in range(4):
    key = input("Enter key " + str(i+1) + " for dict 1: ")
    value = int(input("Enter value " + str(i+1) + " for dict 1: "))
    myDict1[key] = value

# Get input for myDict2
for i in range(4):
    key = input("Enter key " + str(i+1) + " for dict 2: ")
    value = int(input("Enter value " + str(i+1) + " for dict 2: "))
    myDict2[key] = value

combinedDict = combineDictionaries(myDict1, myDict2)

print("Combined Dictionary: " + str(combinedDict))
