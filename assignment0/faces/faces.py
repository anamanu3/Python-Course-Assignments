def convert(variable):
    variable
    if ":)" or ":(" in variable:
        print (variable.replace(":)", "🙂"). replace(":(", "🙁"))
    else:
        print (variable)

variable = input("Hey, how are you?  ")
convert(variable)

