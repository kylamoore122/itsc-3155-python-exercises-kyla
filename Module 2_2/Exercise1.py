# Author: Kyla Moore
# Course: ITSC 3155

def filterUniques(list):
    exists = False
    uniques = []

    # For each element in the original list
    for i in range(len(list)):
        # For each element in the unique list
        for ii in range(len(uniques)):
            # If the element already exists in the unique list
            if list[i] == uniques[ii]:
                exists = True
        # Append to unique list if exists boolean is false
        if exists == True:
            print(str(list[i]) + " is not unique!")
        else:
            print(str(list[i]) + " is unique!")
            uniques.append(list[i])
        # Reset exists boolean
        exists = False

    return uniques

myList = []
uniqueList = []
listSize = 0
element = 0

listSize = int(input("Enter the size of a list (1-10): "))

for i in range(listSize):
    element = int(input("Enter a element #" + str(i+1) + ": "))
    myList.append(element)

uniqueList = filterUniques(myList)

print("Unique List: " + str(uniqueList))