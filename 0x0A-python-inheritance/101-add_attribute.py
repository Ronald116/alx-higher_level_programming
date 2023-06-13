#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible:
"""

def add_new_attribute(obj, attribute, value):
    """if possible, adds new attribute"""

    if not hasattr(obj, attribute):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)

