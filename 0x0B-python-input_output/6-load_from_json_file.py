#!/usr/bin/python3

import json

"""
Create object from a json file
"""

def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”:
    """

    with open(filename, "r") as file:

        obj = json.load(file)

        return obj
