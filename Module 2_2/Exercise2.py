# Author: Kyla Moore
# Course: ITSC 3155

def combineDictionaries(dict1, dict2):
    newDict = {}
    exists = False

    for ch in dict1:
        key1 = ch
        value1 = dict1[ch]
        for ch2 in dict2:
            value2 = dict2[ch2]
            if (ch == ch2):
                newDict[key1] = value1
                newDict[key1] += value2


    return newDict

myDict1 = {}
#myDict1 = {'a':5, 'b':12, 'c':3, 'd':9}
myDict2 = {}
#myDict2 = {'b':4, 'c':9, 'd':10, 'e':16}
combinedDict = {}
key = ''
value = 0
size = 4

# Get input for myDict1
for i in range(size):
    key = input("Enter key " + str(i+1) + " for dict 1: ")
    value = int(input("Enter value " + str(i+1) + " for dict 1: "))
    myDict1[key] = value

# Get input for myDict2
for i in range(size):
    key = input("Enter key " + str(i+1) + " for dict 2: ")
    value = int(input("Enter value " + str(i+1) + " for dict 2: "))
    myDict2[key] = value

combinedDict = combineDictionaries(myDict1, myDict2)

print("Combined Dictionary: " + str(combinedDict))
