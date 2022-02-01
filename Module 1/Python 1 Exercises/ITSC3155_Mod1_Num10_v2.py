#Excercise 10
word = ""
characters = []
charChunk = []
charChunks = []
count = 1

word = input("Enter a string: ")

for ch in word:
    characters.append(ch)

print("Characters: [", end="")
for i in range(len(characters)):
    if i == len(characters)-1:
        print(str(characters[i]), end="")
    else:
        print(str(characters[i]), end=", ")
print("]")

for ch in characters:
    print("Looking at " + ch + "...")
    #print(str(count))
    if count == 3:
        charChunk.append(ch)
        print("Saving chunk..." + str(charChunk))
        charChunks.append(charChunk.copy())
        charChunk.clear()
        count = 1
    elif count < 3:
        print("Character " + ch + " going to chunk...")
        charChunk.append(ch)
        count += 1
print("Saving chunk..." + str(charChunk))
charChunks.append(charChunk.copy())
charChunk.clear()
count = 0


print("Character Chunks: [", end="")
for i in range(len(charChunks)):
    if i == len(charChunks)-1:
        print(str(charChunks[i]), end="")
    else:
        print(str(charChunks[i]), end=", ")
print("]")
