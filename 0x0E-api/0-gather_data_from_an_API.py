#!/usr/bin/python3
""" returns information about employee TO DO list progress"""


import requests
from sys import argv


if __name__ == "__main__":

    userID = argv[1]
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userID)).json()
    name = userInfo.get('name')
    taskCount = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos?completed=true'.
        format(userID)).json()
    taskList = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userID)).json()

    print('Employee {} is done with tasks({}/{}):'.format(
           name, len(taskCount), len(taskList)))
    for item in taskCount:
        print('/t {}'.format(item.get('title')))
