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
            raise(TypeError("size must be an integer"))
        elif size < 0:
            raise(ValueError("size must be >= 0"))

    def area(self):
        """return the Square area"""
        return self.__size * self.__size
