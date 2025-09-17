import re


def main():
    ip_address = input("IPv4 Address: ").strip()
    print(validate(ip_address))


def validate(ip):
    try:
        first, second, third, fourth = ip.split(".")
        for part in (first, second, third, fourth):
            if len(part) > 1 and part[0] == "0":
                return False
            if not part.isdigit():
                return False
        if 0 <= int(first) <= 255 and 0 <= int(second) <= 255 and 0 <= int(third) <= 255 and 0 <= int(fourth) <= 255:
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
