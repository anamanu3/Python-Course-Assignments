import sys
import csv
from tabulate import tabulate

filename = sys.argv[1]

if len(sys.argv) != 2:
    sys.exit("File does not exist")
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")


info = []

try:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for line in reader:
            info.append(line)
    print(tabulate(info, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
