import pytest
from working import convert

def test_nomin():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_60error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_omit_to():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
         convert("13:00 AM to 17:00 PM")
