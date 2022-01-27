phrase = ""
lowerPhrase = ""
upperPhrase = ""
reversedPhrase = ""

phrase = input("What do you have to say?: ")

for ch in phrase:
    if ch.isspace() == False:
        if ch.islower():
            lowerPhrase = lowerPhrase + ch
        if ch.isupper():
            upperPhrase = upperPhrase + ch

reversedPhrase = lowerPhrase + upperPhrase

print(reversedPhrase)