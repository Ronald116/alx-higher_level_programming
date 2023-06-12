#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a class that inherits parent class BaseGeometry"""

    def __init__(self, width, height):
        """initializes the class rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

