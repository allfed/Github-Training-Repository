"""Tests to calculate_circle_area function"""

import math
from src.numerical import calculate_circle_area


def test_calculate_circle_area():
    """
    Test with a positive radius, typical input
    Test with radius 0, edge case
    """
    radius = 5
    expected_result = math.pi * radius**2

    assert calculate_circle_area(radius) == expected_result
    assert calculate_circle_area(0) == 0
