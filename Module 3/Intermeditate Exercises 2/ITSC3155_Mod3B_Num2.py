# Author: Kyla Moore
# Created: 01/28/2022
# Course: ITSC 3155

# Recurse function logic accessed on 2/1/2022 from:
# <https://www.programiz.com/python-programming/examples/fibonacci-recursion>

import time

# I was close before, but I need to practice writing recurive methods
def calculateFibonacci(num):
    # When the number reaches down to 1 or below, end the function
    # Else, since number is the max value, count down and add by 2 and 1 as according to fibonacci definition
    if num <= 1:
        return num
    else:
        return calculateFibonacci(num-2) + calculateFibonacci(num-1)

timeTicked = time.time()
fibonacciNumber = calculateFibonacci(35)
timeTicked = time.time() - timeTicked

print("Fibonacci Calculated: " + str(fibonacciNumber))
print("Time Lapsed: " + str(timeTicked))
