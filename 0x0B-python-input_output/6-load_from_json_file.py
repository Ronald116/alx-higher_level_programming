#!/usr/bin/python3


"""
Create object from a json file
"""

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”:
    """

    with open(filename) as file:

        obj = json.load(file)

        return obj
