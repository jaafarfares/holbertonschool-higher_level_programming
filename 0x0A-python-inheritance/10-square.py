#!/usr/bin/python3
"""Write a class Square
that inherits from Rectangl
(9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """declare a class square that inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
