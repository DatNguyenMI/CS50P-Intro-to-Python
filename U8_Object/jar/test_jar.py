from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-10)
    with pytest.raises(ValueError):
        Jar("cat")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit (500)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw (10)

