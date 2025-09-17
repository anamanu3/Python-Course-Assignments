def main():
    string = input("Say something 😊: ")
    print(shorten(string))


def shorten(sentence):
    no_vowels = ""

    for i in sentence:
        if i not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            no_vowels = no_vowels + i
    return no_vowels


if __name__ == "__main__":
    main()
