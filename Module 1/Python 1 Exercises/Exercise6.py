#Exercise 6

row = 0
col = 0
count = 0

row = int(input("Enter a row num from 1 to 5: "))
col = int(input("Enter a col num from 1 to 5: "))

print("", end="")
for i in range(1, 6):
    #print("R" + str(i))
    for ii in range(1, 6):
        #print("C" + str(ii))
        #When list reaches end
        if i == 5 and ii == 5:
            #When row and column match
            if i == row and ii == col:
                print(str(1), end="")
                count += 1
            else:
                print(str(0), end="")
                count += 1
        #If list is continuing
        else:
            #When row and column match
            if i == row and ii == col:
                print(str(1), end=", ")
                count += 1
            else:
                print(str(0), end=", ")
                count += 1

    #print(" Count: " + str(count))
    if count == 5:
        print("", end="\n")
        count = 0
print("")

