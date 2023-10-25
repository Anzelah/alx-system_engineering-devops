#!/usr/bin/python3
"""Defines a module"""

import json
import requests
import sys


def tabulate_tasks(eid):
    """Populate tasks from the jsonplaceholder api"""
    url = f"https://jsonplaceholder.typicode.com/users/{eid}"
    res = requests.get(url)
    users = res.json()
    name = users.get("username")  # find employee name

    url = f"https://jsonplaceholder.typicode.com/users/{eid}/todos"
    res = requests.get(url)
    tasks = res.json()

    all_tasks = []
    filename = ("{}.json" .format(eid))
    for t in tasks:
        t_dict = {}
        t_dict["task"] = t.get("title")
        t_dict["completed"] = t.get("completed")
        t_dict["username"] = t.get("username")
        all_tasks.append(t_dict)
    data = {"{}" .format(eid): all_tasks}

    with open(filename, mode='w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    tabulate_tasks(sys.argv[1])
