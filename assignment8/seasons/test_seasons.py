from datetime import date
from seasons import SeasonsApp

def test_parse_birthdate_is_good():
    app = SeasonsApp()
    assert app.parse_birthday_date("2000-01-01") == date(2000, 1, 1)

def test_minutes_since_birth_one_day():
    app = SeasonsApp(today=date(2025, 1, 2))
    assert app.minutes_since_birth(date(2025, 1, 1)) == 1440

def test_minutes_to_english_words_simple():
    app = SeasonsApp()
    assert app.minutes_to_english_words(1440) == "One thousand, four hundred forty"
