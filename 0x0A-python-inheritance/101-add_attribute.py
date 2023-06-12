#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible:
"""

def add_new_attribute(obj, attribute, value):
    if not hasattr(obj, attribute):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

