def main():
    while True:
        fraction = input("How much is left in your tank? (type a fraction): ")
        try:
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            print("Please enter a valid fraction :)")



def convert(fraction: str) -> int:
    if "." in fraction or "-" in fraction:
        raise ValueError("Invalid fraction")

    try:
        decimal = eval(fraction)
        if not (0 <= decimal <= 1):
            raise ValueError("Invalid fraction")
    except NameError:
        raise ValueError("Invalid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

    return round(decimal * 100)


def gauge(percent: int) -> str:
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()
