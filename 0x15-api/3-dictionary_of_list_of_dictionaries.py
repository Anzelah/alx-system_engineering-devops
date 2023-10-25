#!/usr/bin/python3
"""Defines a module"""

import json
import requests
import sys


def tabulate_tasks():
    """Populate tasks from the jsonplaceholder api"""
    eid = 1
    data = {}
    while True:
        url = f"https://jsonplaceholder.typicode.com/users/{eid}"
        res = requests.get(url)
        users = res.json()
        if len(users) == 0:
            break
        name = users.get("username")  # find employee name

        url = f"https://jsonplaceholder.typicode.com/users/{eid}/todos"
        res = requests.get(url)
        tasks = res.json()

        all_tasks = []
        for t in tasks:
            t_dict = {}
            t_dict["task"] = t.get("title")
            t_dict["completed"] = t.get("completed")
            t_dict["username"] = name
            all_tasks.append(t_dict)

        data[eid] = all_tasks
        eid += 1

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    tabulate_tasks()
