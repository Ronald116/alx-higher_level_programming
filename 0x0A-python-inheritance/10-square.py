#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """a child class inheriting a parent class(Rectangle)"""

    def __init__(self, size):
        """initializes size of square class"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """implement area of the square class"""
        return size.__size ** 2
