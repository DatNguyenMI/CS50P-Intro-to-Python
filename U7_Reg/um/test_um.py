import pytest
from um import count

def test_um():
    assert count("um it's yummy") == 1

def test_wrap_around():
    assert count("um.... it's yummy") == 1

def test_omit_to():
    assert count("it's yummy UM let me UM think") == 2


