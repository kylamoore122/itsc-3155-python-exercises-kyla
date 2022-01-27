phrase = ""
reversedPhrase = ""

phrase = input("What do you have to say?: ")

for ch in phrase:
    reversedPhrase = ch + reversedPhrase

print(reversedPhrase)