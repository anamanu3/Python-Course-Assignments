from numb3rs import validate

def test_validate_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True

def test_validate_invalid_numbers():
    assert validate("256.100.50.25") == False
    assert validate("192.168.1.999") == False
    assert validate("-1.2.3.4") == False

def test_validate_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("...") == False
