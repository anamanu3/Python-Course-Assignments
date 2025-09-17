import re
import sys

times = {
    "01:00 PM": "13:00", "1:00 PM": "13:00", "1 PM": "13:00",
    "02:00 PM": "14:00", "2:00 PM": "14:00", "2 PM": "14:00",
    "03:00 PM": "15:00", "3:00 PM": "15:00", "3 PM": "15:00",
    "04:00 PM": "16:00", "4:00 PM": "16:00", "4 PM": "16:00",
    "05:00 PM": "17:00", "5:00 PM": "17:00", "5 PM": "17:00",
    "06:00 PM": "18:00", "6:00 PM": "18:00", "6 PM": "18:00",
    "07:00 PM": "19:00", "7:00 PM": "19:00", "7 PM": "19:00",
    "08:00 PM": "20:00", "8:00 PM": "20:00", "8 PM": "20:00",
    "09:00 PM": "21:00", "9:00 PM": "21:00", "9 PM": "21:00",
    "10:00 PM": "22:00", "10 PM": "22:00",
    "11:00 PM": "23:00", "11 PM": "23:00",
    "12:00 AM": "00:00", "12 AM": "00:00",
    "12:00 PM": "12:00", "12 PM": "12:00",
}

def main():
    time = input("Hours: ")
    print(convert(time))



def convert(t):
    matches = re.match(r"^(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)$", t)
    if not matches:
        raise ValueError("Invalid format")


    start = matches.group(1)
    start_AMPM = matches.group(2)
    end = matches.group(3)
    end_AMPM = matches.group(4)

    if ":" not in start:
        start += ":00"
    if ":" not in end:
        end += ":00"

    def to_24h(time, ampm):
        h, m = time.split(":")
        h, m = int(h), int(m)

        if not (1 <= h <= 12) or not (0 <= m <= 59):
            raise ValueError("Invalid time")

        if ampm == "AM":
            if h == 12:
                h = 0
        else:
            if h != 12:
                h += 12

        return f"{h:02}:{m:02}"

    starttime = to_24h(start, start_AMPM)
    endtime = to_24h(end, end_AMPM)

    return starttime + " to " + endtime


if __name__ == "__main__":
    main()
