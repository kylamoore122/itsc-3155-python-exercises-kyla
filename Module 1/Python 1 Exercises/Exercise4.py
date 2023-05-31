#Exercise 4

number = 0
number = int(input("Enter a number: "))
num = 0
nums = []
total = 0
average = 0

for i in range(number):
    num = float(input("Enter number " + str(i+1) + ": "))
    nums.append(num)
    total += num

print("Numbers: ", nums)

average = total / number

print("Average: " + str(average))