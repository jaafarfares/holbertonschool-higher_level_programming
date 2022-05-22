#!/usr/bin/python3
"""
a python program
that print a square area
with a '#'
charachter """


def print_square(size):
    """check if the the size is not an integer
    and check if the size in less then 0
    """
    if type(size) is not int:
        raise(TypeError("size must be an integer"))
    if size < 0:
        raise(ValueError("size must be >= 0"))
    for j in range(1, size+1):
        for j in range(1, size+1):
            print("#", end="")
        print()
