"""
Tests for src/numerical.py
"""

from src.numerical import multiply


def test_multiply_int():
    """
    Tests multiply function using integer inputs.
    """
    test_case = multiply(4, 6)
    assert test_case == 24


def test_multiply_float():
    """
    Tests multiply function using float inputs.
    """
    test_case = multiply(2.5, 3.0)
    assert test_case == 7.5
