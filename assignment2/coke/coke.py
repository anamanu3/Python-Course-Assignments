amount_due = 50


while amount_due > 0:
    print(f"Amount due: {amount_due}")

    coin = int(input("What is the value of your coin?: "))

    if coin == 25 or coin == 10 or coin == 5 or coin == 1:
        amount_due = amount_due - coin
    else:
        print("Not a valid coin")


if amount_due < 0:
    change = abs(amount_due)
    print(f"Change owed: {change}")
elif amount_due == 0:
    print("Change owed: 0")
