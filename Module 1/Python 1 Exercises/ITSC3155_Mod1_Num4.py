#Excercise 4
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

print("List: [", end="")
for i in range(number):
    if i == number-1:
        print(str(nums[i]), end="")
    else:
        print(str(nums[i]), end=", ")
print("]")

average = total / number

print("Average: " + str(average))
