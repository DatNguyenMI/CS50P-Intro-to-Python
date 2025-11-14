import pytest
from numb3rs import validate

def test_nondigit():
    assert validate("cat.py") == False

def test_leading_0():
    assert validate("001.1.1.1") == False

def test_higher_235():
    assert validate("1.1.1.999") == False

def test_not_ip4():
    assert validate("25.35.0.0.0") == False
