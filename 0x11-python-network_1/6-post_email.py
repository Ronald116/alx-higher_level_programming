#!/usr/bin/python3
"""
A python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    req = requests.post(url, data=data)
    print(req.text)
