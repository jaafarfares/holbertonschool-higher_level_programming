#!/usr/bin/python3
""" a simple programme that add tow integer
check for 'a' and 'b'
if they not integer
and
return a + b """


def add_integer(a, b=98):
    """ a function to add tow integer and
    raise an Error if the a
    or b is not an integer"""
    if not isinstance(a, (int, float)):
        """ check if 'a' not an integer"""
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        """ check if 'b' not an integer"""
        raise TypeError("b must be an integer")
    """ if 'a' or 'b' is a float cast it to an int"""
    a = int(a)
    b = int(b)
    return a + b
