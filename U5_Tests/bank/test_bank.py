import pytest
from bank import value
def test_greeting():
    assert value("Hello") == 0
    assert value ("How are you") == 20
    assert value ("What's up") ==100


