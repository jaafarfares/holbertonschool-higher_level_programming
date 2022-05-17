#!/usr/bin/python3
"""ass Square that defines a square."""


class Square:
    """declare the class"""
    def __init__(self, size=0):
        """assgin the value"""
        self.__size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value"""
        if not isinstance(value, (int)):
            raise(TypeError("size must be an integer"))
        elif value < 0:
            raise(ValueError("size must be >= 0"))
        else:
            """return the value"""
            self.__size = value

    def area(self):
        """return the Square area"""
        return self.__size * self.__size

    def my_print(self):
        """print the Square with hachtag charachter"""
        for i in range(self.__size):
            for a in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
