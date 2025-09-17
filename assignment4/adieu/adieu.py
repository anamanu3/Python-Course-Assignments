import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip()
        if not name:
            continue
        names.append(name)
    except EOFError:
        break

names_str = p.join(names)
print(f"\nAdieu, adieu, to {names_str}")
