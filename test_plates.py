from plates import is_valid

def test_starting():
    assert is_valid("CS") == True
    assert is_valid("D") == False
    assert is_valid("F1") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("AAB321") == True
    assert is_valid("ABCD321") == False

def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False

def test_characters():
    assert is_valid("outoftime") == False
    assert is_valid("hello world") == False
    assert is_valid("excuse me") == False

def test_alphanumeric():
    assert is_valid("CS@50") == False
    assert is_valid("GE#12P") == False
    assert is_valid("LJF*2O") == False