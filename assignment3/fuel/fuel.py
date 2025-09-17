def get_frac(fraction):
    while True:
        fraction = input("How much is left in your tank? (type a fraction): ")

        if "." in fraction or "-" in fraction:
            print("Please enter a valid fraction :)")
            continue

        else:
            try:
                decimal = eval(fraction)
                if not (0 <= decimal <= 1):
                    print("Please enter a valid fraction :)")
                    continue
            except NameError:
                print("Please enter a valid fraction :)")
                continue
            except ZeroDivisionError:
                print("Please enter a valid fraction :)")
                continue
            return decimal


decimal = get_frac(None)
percent = round(decimal * 100)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print (f"{percent}%")




