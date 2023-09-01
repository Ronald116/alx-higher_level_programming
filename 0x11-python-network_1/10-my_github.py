#!/usr/bin/python3
"""
 a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, access_token)

    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
