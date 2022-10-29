from bank import value

def test_hello():
    assert value("Hello, world") == 0
    assert value("hello my friend") == 0
    assert value("HELLO PETER") == 0

def test_h():
    assert value("Hey boy") == 20
    assert value("how is it") == 20
    assert value("HEHEHE") == 20

def test_others():
    assert value("What's up") == 100
    assert value("what's going on") == 100
    assert value("MEOW") == 100