import pytest
from fuel import convert, gauge

def test_convert_empty():
    assert convert("0/1") == 0
    assert convert("1/100") == 1
    assert convert("0/2") == 0

def test_convert_full():
    assert convert("100/100") == 100
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"
    assert gauge(75) == "75%"

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")