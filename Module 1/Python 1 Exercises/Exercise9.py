#Exercise 9

words = []
word = ""

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

print("Words: ", words)

for i in range(len(words)):
    print(words[i], end=" ")

print("")