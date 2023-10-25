#!/usr/bin/python3
"""Defines a module"""

import csv
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

    filename = ("{}.csv" .format(eid))
    with open(filename, mode='w') as f:
        for t in tasks:
            completed = t.get("completed")
            titles = t.get("title")
            data = ("\"{}\",\"{}\",\"{}\",\"{}\"\n"
                    .format(eid, name, completed, titles))

            f.write(data)


if __name__ == "__main__":
    tabulate_tasks(sys.argv[1])
