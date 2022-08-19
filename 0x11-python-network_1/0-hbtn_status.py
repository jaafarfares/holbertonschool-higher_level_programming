#!/usr/bin/python3
"""
fetch an url using urlllib package was fun!
"""
from contextlib import contextmanager
import urllib
import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:
    ok = f.read()
    print("Body response:")
    print("\t- type: {}".format(type(ok)))
    print("\t- content: {}".format(ok))
    print("\t- utf8 content: {}".format(ok.decode("utf-8")))
