#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""
import urllib.parse
import urllib
import urllib.request
from sys import argv


ur = argv[1]
maiil = {
        'email': argv[2]
    }
data = urllib.parse.urlencode(maiil)
data = data.encode('ascii')
al = urllib.request.Request(ur, data)
with urllib.request.urlopen(al) as f:
    print(i.read().decode('utf-8'))
