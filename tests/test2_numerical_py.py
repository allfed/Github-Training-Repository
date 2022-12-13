from src.numerical import add_numbers
import pytest

def test_typical():
    assert add_numbers(4, 8) == 12
    assert add_numbers(4.3, 9.2) == 13.5
    assert add_numbers(-2, -3) == -5

def test_raises():
    with pytest.raises(NotImplementedError):
        add_numbers("23", 3)

    with pytest.raises(NotImplementedError):
        add_numbers(23, "5.1")
