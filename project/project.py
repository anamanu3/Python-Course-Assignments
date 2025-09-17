#CS50 Final project - Workout Log
#Ana Manu
#GitHub username: anamanu3
#edX username: anam_manu3
#New York, US
#Date: 20250916






































import csv
from datetime import date, timedelta

def read_workouts(path):
    rows = []
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append({
                    "date": r["date"],
                    "type": r["type"],
                    "distance_km": float(r["distance_km"]),
                    "duration_min": float(r["duration_min"]),
                    "lift_day": r["lift_day"],
                    "notes": r["notes"],
                })
    except FileNotFoundError:
        return []
    return rows

def save_workouts(path, rows):
    with open(path, "w", newline="") as f:
        fieldnames = ["date", "type", "distance_km", "duration_min", "lift_day", "notes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def add_workout(rows, date_str, wtype, distance_km, duration_min, lift_day, notes):
    rows.append({
        "date": date_str,
        "type": wtype,
        "distance_km": float(distance_km),
        "duration_min": float(duration_min),
        "lift_day": lift_day,
        "notes": notes,
    })
    return rows

def weekly_km(rows, week_start_str):
    start = date.fromisoformat(week_start_str)
    end = start + timedelta(days=6)
    total = 0.0
    i = 0
    while i < len(rows):
        r = rows[i]
        if r["type"] == "run":
            d = date.fromisoformat(r["date"])
            if start <= d <= end:
                total += r["distance_km"]
        i += 1
    return round(total, 2)

def pace_min_per_km(distance_km, duration_min):
    if distance_km <= 0:
        raise ValueError("distance must be > 0")
    return round(duration_min / distance_km, 2)

def best_5k(rows):
    best = None
    i = 0
    while i < len(rows):
        r = rows[i]
        if r["type"] == "run" and round(r["distance_km"], 1) == 5.0:
            t = r["duration_min"]
            if best is None or t < best:
                best = t
        i += 1
    return best

def week_dates(start_str):
    d0 = date.fromisoformat(start_str)
    out = []
    i = 0
    while i < 7:
        out.append((d0 + timedelta(days=i)).isoformat())
        i += 1
    return out

def read_pbs(path):
    rows = []
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append({"date": r["date"], "workout": r["workout"], "notes": r["notes"]})
    except FileNotFoundError:
        return []
    return rows

def save_pbs(path, rows):
    with open(path, "w", newline="") as f:
        fieldnames = ["date", "workout", "notes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def add_pb(rows, date_str, workout, notes):
    rows.append({"date": date_str, "workout": workout, "notes": notes})
    return rows

def read_goals(path):
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                return {
                    "calories": int(r["calories"]),
                    "protein_g": int(r["protein_g"]),
                    "carbs_g": int(r["carbs_g"]),
                    "fat_g": int(r["fat_g"]),
                }
    except FileNotFoundError:
        return None

def save_goals(path, g):
    with open(path, "w", newline="") as f:
        fieldnames = ["calories", "protein_g", "carbs_g", "fat_g"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(g)

def ask_date():
    while True:
        s = input("Date (YYYY-MM-DD): ").strip()
        try:
            date.fromisoformat(s)
            return s
        except ValueError:
            print("Please type a date like 2025-05-15.")

def ask_distance_km():
    while True:
        s = input("Distance km (0 if none): ").strip()
        try:
            km = float(s)
            if km < 0:
                print("Distance must be 0 or more.")
                continue
            return km
        except ValueError:
            print("Please enter a number like 5 or 7.5.")

def ask_duration_min():
    while True:
        s = input("Duration (minutes or mm:ss): ").strip()
        if ":" in s:
            parts = s.split(":")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                mins = int(parts[0])
                secs = int(parts[1])
                return round(mins + secs / 60, 2)
            else:
                print("Please use mm:ss like 27:30.")
                continue
        try:
            m = float(s)
            if m <= 0:
                print("Duration must be > 0.")
                continue
            return m
        except ValueError:
            print("Please enter minutes like 45 or time like 27:30.")

def ask_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Please enter a whole number.")

def print_row(cols, widths):
    out = []
    i = 0
    while i < len(widths):
        w = widths[i]
        txt = ""
        if i < len(cols):
            txt = str(cols[i])
        out.append(txt[:w].ljust(w))
        i += 1
    print(" | ".join(out))

def show_week_table(rows, start_str):
    days = week_dates(start_str)
    print("")
    print(f"Week starting {start_str}")
    print("")
    widths = [10, 6, 22, 40]
    print_row(["Date", "Type", "Details", "Notes"], widths)
    print("-" * (sum(widths) + 9))
    i = 0
    while i < len(days):
        d = days[i]
        day_rows = []
        j = 0
        while j < len(rows):
            r = rows[j]
            if r["date"] == d:
                day_rows.append(r)
            j += 1
        if len(day_rows) == 0:
            print_row([d, "", "", ""], widths)
        else:
            k = 0
            while k < len(day_rows):
                r = day_rows[k]
                if r["type"] == "run":
                    det = f'{r["distance_km"]} km, {r["duration_min"]} min'
                else:
                    det = r["lift_day"]
                print_row([d, r["type"], det, r["notes"]], widths)
                k += 1
        i += 1

def pause():
    input("\nPress Enter to return to the menu...")

def show_main():
    print("\nWorkout Log")
    print("1) add workout")
    print("2) weekly workouts")
    print("3) PBs")
    print("4) calorie and macro goals")
    print("5) delete")
    print("6) quit")

def delete_workout_interactive(workouts):
    d = ask_date()
    t = ""
    while t not in ("run", "lift"):
        t = input("Type to delete (run/lift): ").strip().lower()
        if t not in ("run", "lift"):
            print("Please type run or lift.")
    matches = []
    i = 0
    while i < len(workouts):
        r = workouts[i]
        if r["date"] == d and r["type"] == t:
            matches.append((i, r))
        i += 1
    if len(matches) == 0:
        print("No match.")
        return workouts
    print("\nChoices:")
    widths = [4, 10, 22, 40]
    print_row(["#", "Date", "Details", "Notes"], widths)
    print("-" * (sum(widths) + 9))
    j = 0
    while j < len(matches):
        idx, r = matches[j]
        if r["type"] == "run":
            det = f'{r["distance_km"]} km, {r["duration_min"]} min'
        else:
            det = r["lift_day"]
        print_row([j + 1, r["date"], det, r["notes"]], widths)
        j += 1
    while True:
        pick = input("Delete which #? ").strip()
        if pick.isdigit():
            n = int(pick)
            if 1 <= n <= len(matches):
                real_index = matches[n - 1][0]
                del workouts[real_index]
                print("Deleted.")
                return workouts
        print("Please pick a valid number.")

def delete_pb_interactive(pbs):
    key = input("Which workout PB to delete (name): ").strip().lower()
    matches = []
    i = 0
    while i < len(pbs):
        r = pbs[i]
        if r["workout"].strip().lower() == key:
            matches.append((i, r))
        i += 1
    if len(matches) == 0:
        print("No match.")
        return pbs
    print("\nChoices:")
    widths = [4, 10, 20, 50]
    print_row(["#", "Date", "Workout", "Notes"], widths)
    print("-" * (sum(widths) + 9))
    j = 0
    while j < len(matches):
        idx, r = matches[j]
        print_row([j + 1, r["date"], r["workout"], r["notes"]], widths)
        j += 1
    while True:
        pick = input("Delete which #? ").strip()
        if pick.isdigit():
            n = int(pick)
            if 1 <= n <= len(matches):
                real_index = matches[n - 1][0]
                del pbs[real_index]
                print("Deleted.")
                return pbs
        print("Please pick a valid number.")

def main():
    workouts_path = "workouts.csv"
    pbs_path = "pbs.csv"
    goals_path = "goals.csv"

    workouts = read_workouts(workouts_path)
    pbs = read_pbs(pbs_path)

    while True:
        show_main()
        choice = input("Choice: ").strip()

        if choice == "1":
            d = ask_date()
            kind = ""
            while kind not in ("run", "lift"):
                kind = input("Type (run/lift): ").strip().lower()
                if kind not in ("run", "lift"):
                    print("Please type run or lift.")
            if kind == "run":
                dist = ask_distance_km()
                mins = ask_duration_min()
                notes = input("Notes: ").strip()
                workouts = add_workout(workouts, d, "run", dist, mins, "", notes)
            else:
                day = input("Lift day (chest/back/legs/etc): ").strip()
                notes = input("Notes: ").strip()
                workouts = add_workout(workouts, d, "lift", 0.0, 0.0, day, notes)
            save_workouts(workouts_path, workouts)
            print("Saved.")
            pause()

        elif choice == "2":
            start = input("Week start (YYYY-MM-DD): ").strip()
            try:
                date.fromisoformat(start)
                show_week_table(workouts, start)
                total = weekly_km(workouts, start)
                print("")
                print(f"Weekly run km: {total}")
            except ValueError:
                print("Bad date.")
            pause()

        elif choice == "3":
            while True:
                print("\nPBs")
                print("1) add PB")
                print("2) see all PBs")
                print("3) back")
                sub = input("Choice: ").strip()
                if sub == "1":
                    d = ask_date()
                    w = input("What workout did you PB? ").strip()
                    n = input("Notes (type, stats): ").strip()
                    pbs = add_pb(pbs, d, w, n)
                    save_pbs(pbs_path, pbs)
                    print("Saved PB.")
                elif sub == "2":
                    if len(pbs) == 0:
                        print("No PBs yet.")
                    else:
                        widths = [10, 20, 50]
                        print_row(["Date", "Workout", "Notes"], widths)
                        print("-" * (sum(widths) + 6))
                        i = 0
                        while i < len(pbs):
                            r = pbs[i]
                            print_row([r["date"], r["workout"], r["notes"]], widths)
                            i += 1
                elif sub == "3":
                    break
                else:
                    print("Please type 1, 2, or 3.")
            pause()

        elif choice == "4":
            while True:
                print("\nGoals")
                print("1) change goals")
                print("2) see goals")
                print("3) back")
                sub = input("Choice: ").strip()
                if sub == "1":
                    c = ask_int("Calories: ")
                    p = ask_int("Protein g: ")
                    carb = ask_int("Carbs g: ")
                    f = ask_int("Fat g: ")
                    g = {"calories": c, "protein_g": p, "carbs_g": carb, "fat_g": f}
                    save_goals(goals_path, g)
                    print("Saved goals.")
                elif sub == "2":
                    g = read_goals(goals_path)
                    if g is None:
                        print("No goals set.")
                    else:
                        print(f'Calories: {g["calories"]}')
                        print(f'Protein: {g["protein_g"]} g')
                        print(f'Carbs: {g["carbs_g"]} g')
                        print(f'Fat: {g["fat_g"]} g')
                elif sub == "3":
                    break
                else:
                    print("Please type 1, 2, or 3.")
            pause()

        elif choice == "5":
            print("\nDelete")
            print("1) workout")
            print("2) PB")
            sub = input("Choice: ").strip()
            if sub == "1":
                workouts = delete_workout_interactive(workouts)
                save_workouts(workouts_path, workouts)
            elif sub == "2":
                pbs = delete_pb_interactive(pbs)
                save_pbs(pbs_path, pbs)
            else:
                print("Please type 1 or 2.")
            pause()

        elif choice == "6":
            break
        else:
            print("Please type 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
