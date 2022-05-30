#!/usr/bin/python3
""" a class that
sort the list
and print it"""


class MyList(list):
    """the class parameter"""
    def print_sorted(self):
        list = sorted(self)
        print(list)
