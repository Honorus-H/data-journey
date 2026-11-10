""""This program remove the vowel of a word """
word = input("input: ")
new =""
for letter in word:
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        new += letter
print(f"Output: {new}")