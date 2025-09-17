import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        count = 0
        for line in file:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                continue
            count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
