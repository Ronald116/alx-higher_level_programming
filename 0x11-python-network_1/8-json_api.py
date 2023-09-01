#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
Args:
    i. The letter must be sent in the variable q
    ii. If no argument is given, set q=""
    iii. If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    iv. Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
"""

import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    payload = {'q': letter}

    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = req.json()
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
