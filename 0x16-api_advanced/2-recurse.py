#!/usr/bin/python3
"""Defines a module"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list containing titles of all hot articles for given subreddit"""
    
    headers = {'User-Agent': 'MyApi/0.0.1'}
    url = "https://api.reddit.com/r/{}/hot?after=after&count=count".format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        content = r.json().get("data")
        count += content.get("dist")
        after = content.get("after")

        for post in content["children"]:
            hot_list.append(post["data"]["title"])
        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    else:
        return None
