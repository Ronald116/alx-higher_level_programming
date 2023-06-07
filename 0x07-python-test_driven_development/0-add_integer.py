#!/usr/bin/python3
"""

A  module  that adds up 2 integers

"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers

    Args:
        a: first number
        b: second number

    Returns:
        Sum of the two numbers which are integers

    Raises:
        TypeError:  either of the arguments not an integer or a float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b
