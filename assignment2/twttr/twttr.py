string = (input("Say something 😊: "))

no_vowels = ""

for i in string:
    if i not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        no_vowels = no_vowels + i

print(no_vowels)
