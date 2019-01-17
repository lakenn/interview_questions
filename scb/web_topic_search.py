#!/bin/python3

import sys
import os
import urllib.request
import json

import requests


# Complete the function below.

def getTopicCount(topic):
    url = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={}'.format(topic)
    re = requests.get(url=url)
    result = re.json()
    html_content = result['parse']['text']['*']
    return html_content.count(topic)


f = open(os.environ['OUTPUT_PATH'], 'w')

try:
    _topic = str(input())
except:
    _topic = None

res = getTopicCount(_topic)
f.write(str(res) + "\n")

f.close()
