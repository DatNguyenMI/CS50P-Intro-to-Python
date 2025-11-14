
import pytest
from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("H") == False

def test_begin_alphabet():
    assert is_valid("AS15") == True
    assert is_valid("50AS") == False
    assert is_valid("50") == False   
    assert is_valid("A5") == False


def test_number_placement():
    assert is_valid("PS42") == True
    assert is_valid("PS42S") == False


def test_number_0():
    assert is_valid("PS420") == True
    assert is_valid("PS042") == False


def test_punctuation():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
