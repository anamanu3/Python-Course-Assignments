from twttr import shorten

def test_shorten_basic():
    assert shorten("hey") == "hy"

def test_shorten_case():
    assert shorten("HELLO") == "HLL"
    assert shorten("TwItTeR") == "TwtTR"

def test_shorten_numbers():
    assert shorten("CS50 2022") == "CS50 2022"

def test_shorten_punctuation():
    assert shorten("hi!") == "h!"
    assert shorten("what's up?") == "wht's p?"
