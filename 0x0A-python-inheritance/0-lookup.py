#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the available attributes and methods of the object.
    """
    attributes = []
    methods = []

    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)

    attributes.sort()
    methods.sort()

    return attributes + methods

