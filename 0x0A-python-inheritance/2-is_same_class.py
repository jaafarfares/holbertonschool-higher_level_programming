#!/usr/bin/python3
"""Write a function that returns True if the object is exactly
an instance of the specified class
otherwise False """


def is_same_class(obj, a_class):
    """the method parameter"""
    return type(obj) is a_class


is_same_class(1, int)
is_same_class(1, object)
