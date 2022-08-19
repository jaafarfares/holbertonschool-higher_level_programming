#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == '__main__':
    maill = {
        'email': argv[2]
    }
    data = p.urlencode(maill)
    data = data.encode('ascii')
    req = r.Request(argv[1], data)
    with r.urlopen(req) as res:
        body = res.read().decode('utf-8')
        print(body)
        