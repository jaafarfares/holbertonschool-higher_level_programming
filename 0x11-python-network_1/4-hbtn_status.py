#!/usr/bin/python3
"""
use the package requests to fetch an url
"""
import requests


if __name__ == '__main__':
    data = requests.get('https://intranet.hbtn.io/status').content
    data = data.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))