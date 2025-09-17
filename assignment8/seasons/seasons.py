from datetime import date
import sys
import inflect


class SeasonsApp:
    def __init__(self, today=None):
        self.today = today if today is not None else date.today()
        self.p = inflect.engine()

    def ask_for_birthday(self):
        return input("Date of Birth (YYYY-MM-DD): ").strip()

    def parse_birthday_date(self, text):
        try:
            return date.fromisoformat(text)
        except ValueError:
            raise ValueError("Input must be YYYY-MM-DD format.")

    def minutes_since_birth(self, birthdate):
        delta = self.today - birthdate
        if delta.days < 0:
            raise ValueError("Birth date in the future!!! :)")
        return delta.days * 24 * 60

    def minutes_to_english_words(self, minutes):
        words = self.p.number_to_words(minutes, andword="")
        return words.capitalize()

    def run(self):
        try:
            birth_text = self.ask_for_birthday()
            birthdate = self.parse_birthday_date(birth_text)
            minutes = self.minutes_since_birth(birthdate)
            words = self.minutes_to_english_words(minutes)
            print(f"{words} minutes")
        except ValueError:
            sys.exit("Invalid date")


def main():
    app = SeasonsApp()
    app.run()


if __name__ == "__main__":
    main()
