import pytest
from seasons import Birthday

def test_invaliddays():
    with pytest.raises(ValueError):
        Birthday ("January 1, 2000")
    with pytest.raises(ValueError):
        Birthday ("2000-14-16")

