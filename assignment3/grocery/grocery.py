items = []

while True:
    try:
        stuff = input().lower()
        items.append(stuff)
    except EOFError:
        break

#getting counts
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

#aplphabetical order with counts
for name in sorted(counts):
    print(counts[name], name.upper())



