#!/usr/bin/python3
"""
displays the value of the X-Request-Id
"""
from sys import argv
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as f:
        print(f.info().get("X-Request-Id"))
