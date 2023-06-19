#!/usr/bin/python3
"""A rectangle class"""
from models.base import Base

class Rectangle(Base):
    """defines a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize class rectangle"""

        self.width = width
        self.heigth = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """gets the value of the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value


    @height.setter
    def height(self, value):
        """gets the value for the height"""
        if type(value) != int:
            raise TypeError("height must be an integer""")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value


    @x.setter
    def x(self, param):
        """sets the param for x"""
        if type(param) != int:
            raise TypeError("x must be an integer")
        if param < 0:
            raise ValueError("x must be >= 0")

        self.__x = param


    @y.setter
    def y(self, param):
        """sets the value for y"""
        if type(param) != int:
            raise TypeError("y must be an integer")
        if param < 0:
            raise ValueError("y must be >= 0")

        self.__y = param


    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle 
        instance with the character #
        """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """update string display of class rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, 
            self.__y, self.__width, self.__height))


    def update(self, *args, **kwargs):
        """assign argument to each value"""
        if len(args) > 0:
            a = 0
            for arg in len(args):
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg

                a = a + 1

        elif len(kwargs) != 0:
            for key, value in len(kwargs).items():
                if  key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value


        def to_dictionary(self):
            """ returns rectangle in dictionary"""
            return {'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y}


