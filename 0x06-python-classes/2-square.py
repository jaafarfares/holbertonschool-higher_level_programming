#!/usr/bin/python3
"""a class Square that defines a square."""


class Square:
    """declare the class"""
    def __init__(self, size=0):
        """assgin the value"""
        self.__size = size
        if isinstance(size, (int)):
            pass
        if not isinstance(size, (int)):
            """if the value not integer"""
            raise(TypeError("size must be an integer"))
        elif size < 0:
            """if the value is less then 0"""
            raise(ValueError("size must be >= 0"))
