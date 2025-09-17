from jar import Jar

def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    j2 = Jar(5)
    assert j2.capacity == 5
    assert j2.size == 0

    try:
        Jar(-1)
        assert False
    except ValueError:
        assert True

def test_str():
    j = Jar()
    assert str(j) == ""
    j.deposit(1)
    assert str(j) == "🍪"
    j.deposit(2)
    assert str(j) == "🍪🍪🍪"

def test_deposit():
    j = Jar(3)
    j.deposit(2)
    assert j.size == 2

    try:
        j.deposit(2)  # over capacity
        assert False
    except ValueError:
        assert True

    try:
        j.deposit(-1)  # negative
        assert False
    except ValueError:
        assert True

def test_withdraw():
    j = Jar(5)
    j.deposit(4)
    j.withdraw(1)
    assert j.size == 3

    try:
        j.withdraw(10)  # too many
        assert False
    except ValueError:
        assert True

    try:
        j.withdraw(-1)  # negative
        assert False
    except ValueError:
        assert True
