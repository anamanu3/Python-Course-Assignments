def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if 2 > len(s) or 6 < len(s):
        return False
    for i,c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return False
            if not s[i:].isnumeric():
                return False
            break
    if not s.isalnum():
        return False
    return True

if __name__ == "__main__":
    main()
