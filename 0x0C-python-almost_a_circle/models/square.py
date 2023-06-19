#!/usr/bin/python3
"""A module class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class square constructor"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None

        super().__init__(self, size, x, y, id)


    def __str__(self):
        """format ffor string display"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".format(self.id,
            self.x, self.y, self.size))

    @property
    def size(self):
        """returns the value of size"""
        return self.__width


    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value


    def update(self, *args, **kwargs):
        """Updates attributes of each arguments"""

        if len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns class square in dict form"""

        return {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}



