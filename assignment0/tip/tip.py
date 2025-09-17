#main function - calls two other functions to change the input into usable floats and then mult them to find the tip you would leave
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#changes input by removing dollar sign if you input $##.## and then changing it to a float
def dollars_to_float(input):
    input = float(input[1:])
    return input


#changes input by removing percent sign, changing it to a float, then changing the decimal places so the percent is a deciaml.
def percent_to_float(input):
    input = float(input[:-1])
    return input/100



main()
