from bank import value

def test_value_default():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, Newman") == 0
    assert value("  Hello there") == 0  # leading spaces

def test_h_only_words():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20
    assert value("H") == 20

def test_other_words():
    assert value("what's up") == 100
    assert value("good morning") == 100
    assert value("yo") == 100
