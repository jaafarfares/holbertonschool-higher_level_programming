#!/usr/bin/python3
""" manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
import urllib
from sys import argv
import urllib.request as r


if __name__ == '__main__':
    data = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(data) as i:
            print(i.read().decode('utf-8'))
    except urllib.error.HTTPError as f:
        print("Error code: {}".format(f.code))
