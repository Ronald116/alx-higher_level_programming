#!/usr/bin/python3

"""a rectangle subclass square"""

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """A grandchild class inherits from parent and grandparent class"""
    def __init__(self, size):
        """initializes class"""

        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size


