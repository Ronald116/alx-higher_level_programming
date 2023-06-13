#!/usr/bin/python3

import json

"""
Save object to a file
"""

def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a 
    text file, using a JSON representation:
    """

    with open(filename, "w") as file:
        json.dumps(my_obj, file)
