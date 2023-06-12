#!/usr/bin/python3

"""A simple class MyList"""

class MyList(list):
    """A class MyList that inherits form list"""

    def print_sorted(self):
        """ prints list in ascending order"""
        print(sorted(self))
