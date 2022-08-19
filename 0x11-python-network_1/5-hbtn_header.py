#!/usr/bin/python3
"""use the packages requests and sys
to fetch a header of url
"""
import requests
from sys import argv


if __name__ == '__main__':
    data = requests.get(argv[1])
    print(data.headers.get('X-Request-Id'))
