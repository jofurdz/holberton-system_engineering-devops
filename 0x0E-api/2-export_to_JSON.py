#!/usr/bin/python3
"""exports data in JSON format"""
from sys import argv
import requests
import json


if __name__ == "__main__":
    userID = argv[1]
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userID)).json()
    username = userInfo.get('username')
    taskCount = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userID)).json()

    jsonTasks = {userID: []}

    for task in taskCount:
        jsonTasks[userID].append({"task": task.get('title'),
                                  "completed": task.get('completed'),
                                  "username": username})

    with open('{}.json'.format(userID), "w") as jsonFile:
        json.dump(jsonTasks, jsonFile)
