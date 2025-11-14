import pytest
from twttr import shorten

def test_1_shorten():
    assert shorten("hello") == "hll"

def test_2_shorten():
    assert shorten ("What's yOUr name") == "Wht's yr nm"

def test_3_shorten():
    assert shorten ("hello 123.") == "hll 123."





