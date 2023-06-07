#!/usr/bin/python3
"""
A module function that prints a square with character '#'
"""

def print_square(size):
    """

    Args:
        size (int):length of the square

    Raises:
        TypeError: size is not an integer
        TypeError: size is a float and less than zero
        ValueError:size is less than zero

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
