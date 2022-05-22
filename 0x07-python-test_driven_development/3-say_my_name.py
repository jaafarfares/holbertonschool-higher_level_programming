#!/usr/bin/python3
""" a programme
that prints
the first name and
the last name
in the same line"""


def say_my_name(first_name, last_name=""):
    """ a function that chekks if
    the value are not a string
    and raise an error if it found it """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
