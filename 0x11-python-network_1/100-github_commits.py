#!/usr/bin/python3
"""
Lists 10 most recents commit
"""

import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?'.format(owner, repo_name)

    response = requests.get(url)

    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                            commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
