import sys
import csv


if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if not sys.argv[2].endswith(".csv"):
    sys.exit("Please create a CSV file to store new data.")



students = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({
                "first": first.lstrip(),
                "last": last.strip(),
                "house": row["house"].strip()
            })

    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

except FileNotFoundError:
    sys.exit("File does not exist")
