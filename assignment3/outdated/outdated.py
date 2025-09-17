months = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}

def get_date():
    while True:
        date = input("Date: ").strip()

        if "," in date:
            date = date.title()
            date2 = date.split(" ")
            date2__1 = date2[1][:-1]

            if not date2[0] in months.keys():
                continue
            if int(date2__1) > 31:
                continue
            if len(date2__1) > 2 or len(date2[2]) > 4:
                print("gets here")
                continue
            if date2[0] in months:
                month = months[date2[0]]
            if len(date2__1) == 1:
                date2_1 = "0" + date2__1
            elif len(date2__1) == 2:
                date2_1 = date2__1
            print(f"{date2[2]}-{month}-{date2_1}")
            break
        elif "/" in date:
            date_2 = date.split("/")

            if not date_2[0].isdigit() or not date_2[1].isdigit() or not date_2[2].isdigit():
                continue
            if len(date_2[2]) != 4:
                print("here")
                continue
            if int(date_2[0]) > 12:
                continue
            if int(date_2[1]) > 31:
                continue
            if len(date_2[0]) > 2 or len(date_2[1]) > 2 or len(date_2[2]) > 4:
                print("here")
                continue
            if len(date_2[0]) == 1:
                date_2_0 = "0" + date_2[0]
            if len(date_2[1]) == 1:
                date_2_1 = "0" + date_2[1]
            if len(date_2[0]) != 1:
                date_2_0 = date_2[0]
            if len(date_2[1]) != 1:
                date_2_1 = date_2[1]
            print(f"{date_2[2]}-{date_2_0}-{date_2_1}")
            break
        else:
            continue


get_date()



