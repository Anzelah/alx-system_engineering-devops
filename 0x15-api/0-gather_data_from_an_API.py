#!/usr/bin/python3
"""Defines a module"""

import requests
import sys


def tabulate_tasks(eid):
    """Populate tasks from the jsonplaceholder api"""
    url = f"https://jsonplaceholder.typicode.com/users/{eid}"
    res = requests.get(url)
    users = res.json()
    name = users.get("name")  # find employee name

    url = f"https://jsonplaceholder.typicode.com/users/{eid}/todos"
    res = requests.get(url)
    tasks = res.json()

    num_tasks = len(tasks)  # number of tasks

    completed = 0
    titles = ""
    for t in tasks:
        if t.get("completed") is True:
            completed += 1  # tasks completed
            titles += "\t " + t.get("title") + "\n"
            # titles of the completed tasks

    print("Employee {} is done with tasks ({}/{}):"
          .format(name, completed, num_tasks))
    print(titles.strip())


if __name__ == "__main__":
    tabulate_tasks(sys.argv[1])
