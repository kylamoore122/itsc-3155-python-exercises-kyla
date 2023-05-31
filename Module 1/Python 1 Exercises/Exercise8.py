#Exercise 8

def isUnique(arg1, arg2):
    print("Checking uniqueness of number...")
    
    unique = True
    strikes = 0
    entries = len(arg2)

    for i in range(entries):
        #print(arg2[i])
        if arg1 == arg2[i]:
            strikes += 1
        
    if strikes > 1:
        print(str(arg1) + " is not unique!")
        unique = False
    else:
        print(str(arg1) + " is unique!")
        
    return unique

number = 0
numbers = []
numbersU = []

for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

for i in numbers:
    if isUnique(i, numbers) == True:
        numbersU.append(i)

print("Numbers: ", numbers)

print("Unique Numbers: ", numbersU)