#!/usr/bin/python3
"""
A module function that prints 'My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):

    '''

    Args:
        first_name (str): The first name
        last_name (str): The last name 

    Raises:
        TypeError: If either the first_name and last_name are not strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".fomat(first_name, last_name))
