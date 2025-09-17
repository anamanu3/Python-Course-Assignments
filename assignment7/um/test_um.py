from um import count

def test_basic():
    assert count("hello, um, world") == 1

def test_case_and_punct():
    assert count("Um... UM? um!") == 3

def test_not_substrings():
    assert count("yummy album aluminum") == 0

def test_spaces():
    assert count("um um") == 2
