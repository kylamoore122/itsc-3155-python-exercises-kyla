#Excercise 7
number = 0
numbers = []

while(number != "QUIT"):
    number = input("Enter a number or QUIT to quit: ")

    if number != "QUIT":
        numbers.append(int(number))

print("List: [", end="")
for i in range(len(numbers)):
    if i == len(numbers)-1:
        print(str(numbers[i]), end="")
    else:
        print(str(numbers[i]), end=", ")
print("]")
