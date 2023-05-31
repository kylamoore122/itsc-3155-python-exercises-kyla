#Exercise 3
import math

integer = 0
integer = int(input("Enter an integer greater than 1: "))

for i in range(integer + 1):
    print("The cube of " + str(i) + " is " + str(pow(i, 3)))