camel = input("camelCase variable: ")


#breaking up the words at upper case letters
words = []

i = 0
start = 0

while i < len(camel):
    if camel[i].isupper():
        words.append(camel[start:i])
        start = i
    i = i + 1

words.append(camel[start:])



#creating new list with completely lowercase words
lower_words = []
for word in words:
    lower_words.append(word.lower())


#making list into joined by _ (snake case)
snake_case = "_".join(lower_words)

print(snake_case)




