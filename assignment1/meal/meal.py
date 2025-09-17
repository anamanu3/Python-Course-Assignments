def main(time):
    time = convert(time)
    if 7 <= time <= 8:
        print ("breakfast time")
    elif 12 <= time <= 13:
        print ("lunch time")
    elif 18 <= time <= 19:
        print ("dinner time")



def convert(time):
     hrs, min = time.split(":")
     hrs = int(hrs)
     min = int(min)
     return (float((hrs + min / 60)))


if __name__ == "__main__":
    time = input("What time is it?: ")
    main(time)
