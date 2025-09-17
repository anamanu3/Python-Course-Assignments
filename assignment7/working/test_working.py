from working import convert
import pytest

def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 2 PM") == "10:00 to 14:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:30 AM to 1:15 PM") == "11:30 to 13:15"
    assert convert("12:45 PM to 3:05 PM") == "12:45 to 15:05"

def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

import pytest  # add this

# ... your existing tests ...

def test_requires_to_word():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("13 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("10:60 AM to 1 PM")

