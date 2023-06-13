#!/usr/bin/python3
""" inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A child class that inherits parent class"""

    def __init__(self, width, height):
        """initialize a new rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
