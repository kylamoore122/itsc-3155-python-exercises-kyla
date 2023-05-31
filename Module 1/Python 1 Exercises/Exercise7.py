#Exercise 7

number = 0
numbers = []
evenNumbers = []

while(number != "QUIT"):
    number = input("Enter a number or QUIT to quit: ")

    if number != "QUIT":
        numbers.append(int(number))

print("Numbers: ", numbers)

for i in range(len(numbers)-1):
    if ((numbers[i] % 2) == 0):
        evenNumbers.append(numbers[i])

print("Even Numbers: ", evenNumbers)
