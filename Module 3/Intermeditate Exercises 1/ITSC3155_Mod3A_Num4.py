# Author: Kyla Moore
# Created: 01/28/2022
# Course: ITSC 3155

entry = None
sum = 0

for i in range(5):
    # Repeat while entry is not an int
    while(type(entry) != int):
        # Get input
        entry = input("Enter int #" + str(i+1) + ": ")

        # Attempt to convert input to int
        try:
            entry = int(entry)
        except ValueError:
            # Check if input is valid, if not print error message
            if type(entry) != int:
                print("Invalid input. Please enter an int.")

    sum += entry
    entry = None

print("Your sum is " + str(sum))
