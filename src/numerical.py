"""Module providing a function that calculate the area of a circle."""
import math


def calculate_circle_area(radius):
    """
    Calculates the area of a circle from its radius.

    Arguments:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """

    area = math.pi * radius * radius
    return area
