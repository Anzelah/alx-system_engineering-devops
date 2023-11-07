#!/usr/bin/python3
"""Defines a module"""

import requests


def number_of_subscribers(subreddit):
    """Retuns number of subscribers for a given subreddit"""
    headers =  {'User-Agent': 'MyApi/0.0.1'}
    
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        subs = res.json()["data"]["subscribers"]
    else:
        subs = 0

    return subs
