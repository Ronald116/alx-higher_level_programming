#!/usr/bin/python3
"""Python script that takes a URL and displays Id variable"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers['X-Request-Id']
        print(header)
