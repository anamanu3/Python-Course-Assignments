from plates import is_valid

def test_begins_with_letters():
    assert is_valid("CS") is True
    assert is_valid("CS50") is True
    assert is_valid("A2345") is False
    assert is_valid("AA234") is True

def test_length():
    assert is_valid("CS") is True
    assert is_valid("CS50") is True
    assert is_valid("C") is False
    assert is_valid("ABCDEFG") is False

def test_number_placement():
    assert is_valid("AAA222") is True
    assert is_valid("CS50A") is False
    assert is_valid("C5S0") is False
    assert is_valid("CS50") is True

def test_zero_placement():
    assert is_valid("CS05") is False
    assert is_valid("AB0") is False
    assert is_valid("CS50") is True

def test_alphanumeric():
    assert is_valid("CS50") is True
    assert is_valid("CS-50") is False
    assert is_valid("CS 50") is False
    assert is_valid("CS!50") is False
