from validator_collection import checkers

email = input("Please type your email: ").strip()

if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")
