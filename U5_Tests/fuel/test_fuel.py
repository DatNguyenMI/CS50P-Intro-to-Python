
import pytest
from fuel import convert, gauge

def test_convert(): #string to integer
    assert convert("25/100") == 25
    assert convert("70/100") == 70

def test_convert_error(): #raise value error for invalid
    with pytest.raises (ValueError):
        convert("110/100")
    with pytest.raises (ValueError):
        convert("X/y")
    with pytest.raises (ZeroDivisionError):
        convert("90/0")
    with pytest.raises (ValueError):
        convert("-90/100")

def test_gauge(): #convert percentage to indicator
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"





