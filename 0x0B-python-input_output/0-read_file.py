#!/usr/bin/python3
"""
A function that reads text file to stdout
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """
    with open(filename, encoding="utf-8") as file:

        content = file.read()
        print(content, end='')
        
