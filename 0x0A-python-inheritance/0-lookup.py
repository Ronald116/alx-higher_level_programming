#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of
    an onject
    """
    return [attr for attr in dir(obj) if not attr.startswith('__')]
