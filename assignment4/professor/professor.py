import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y

        attempts = 0
        while attempts < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == ans:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1

        if attempts == 3:
                print(f"{x} + {y} = {ans}")

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 4 > level > 0:
                break
            else:
                continue
        except ValueError:
            continue
    return level



def generate_integer(level):
    if level == 1:
        one_digit = list(range(0, 10))
        return random.choice(one_digit)
    elif level == 2:
        two_digit = list(range(10, 100))
        return random.choice(two_digit)
    elif level == 3:
        three_digit = list(range(100, 1000))
        return random.choice(three_digit)
    else:
        raise ValueError("level must be 1, 2, or 3")


if __name__ == "__main__":
    main()


