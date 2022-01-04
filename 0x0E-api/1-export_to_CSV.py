#!/usr/bin/python3
"""exports data in the CSV format"""
from sys import argv
import requests
import csv


if __name__ == '__main__':
    userID = argv[1]
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userID)).json()
    username = userInfo.get('username')
    taskCount = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userID)).json()

    with open('{}.csv'.format(userID), 'w') as csvFile:
        csv_write = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in taskCount:
            csv_write.writerow([userID, username, task.get('completed'),
                               task.get('title')])
