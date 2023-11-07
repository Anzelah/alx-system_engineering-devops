#!/usr/bin/python3
"""Defines a module"""

import requests


def top_ten(subreddit):
    """Print titles of first 10 hot topics for a given subreddit"""

    headers = {'User-Agent': 'MyApi/0.0.1'}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        content = r.json()["data"]["children"]
        for post in content:
            print(post["data"]["title"])
    else:
        print(None)
