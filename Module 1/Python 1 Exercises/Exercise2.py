#Exercise 2

stringA = ""
stringB = ""
stringA = input("Enter a string: ") 
stringB = input("Enter another string: ")

if(stringA.endswith(stringB)):
    print(True)
elif(stringB.endswith(stringA)):
    print(True)
else:
    print(False)