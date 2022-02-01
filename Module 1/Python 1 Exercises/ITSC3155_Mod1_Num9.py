#Excercise 9
words = []
word = ""

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

print("List: [", end="")
for i in range(len(words)):
    if i == len(words)-1:
        print(str(words[i]), end="")
    else:
        print(str(words[i]), end=", ")
print("]")
