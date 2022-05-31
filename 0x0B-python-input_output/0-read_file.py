#!/usr/bin/python3
""" Write a function that reads a text file
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """open the file a read the content """

    with open(filename) as f:

        print(f.read(), end="")
