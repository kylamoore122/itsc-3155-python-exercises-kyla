#Exercise 5

def ifExists(arg1, arg2):
    print("Checking existance of number...")
    
    exists = False
    entries = len(arg2)

    for i in range(entries):
        #print(arg2[i])
        if arg1 == arg2[i]:
            exists = True
            print(str(arg1) + " is not unique!")
            break
        
    if exists == False:
        print(str(arg1) + " is unique!")
        
    return exists

list1 = []
list2 = []
listU = []

for i in range(5):
    list1.append(int(input("Enter a number for the first list: ")))
for i in range(5):
    list2.append(int(input("Enter a number for the second list: ")))

print("*** Comparings lists...")
for n2 in range(len(list2)):
    if (ifExists(list2[n2], list1) == True and ifExists(list2[n2], listU) == False):
        #print(list2[n2])
        listU.append(list2[n2])

print("Common List: ", listU)