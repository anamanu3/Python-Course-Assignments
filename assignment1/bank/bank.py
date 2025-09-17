greet = input("Greeting: ").strip()

if greet.startswith("hello") or greet.startswith("hello,") or greet.startswith("Hello,") or greet.startswith("Hello"):
    print("$0")
elif greet.startswith("h") or greet.startswith("H"):
    print ("$20")
else:
    print ("$100")
