import random

numbers = [1]

while True:
    level = int(input("Level: "))

    if level < 1:
        pass
    else:
        break

while level > 2:
    level -= 1
    numbers.append(level)

store = random.choice(numbers)

while True:
    try:
        guess = int(input("Guess: "))

        if store > guess >= 1:
            print("Too small!")
        elif store < guess:
            print("Too large!")
        elif guess == store:
            print("Just right!")
            break
    except ValueError:
        pass



