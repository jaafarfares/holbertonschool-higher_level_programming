#!/usr/bin/python3
"""a python program that defines a rectangle"""


class Rectangle():
    """ empty class rectangle"""
    def __init__(self, width=0, height=0):
        """ the function arguments """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width property """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        elif value < 0:
            raise(ValueError("width must be >= 0"))
        else:
            self.__width = value

    @property
    def height(self):
        """height property"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter """
        if type(value) is not int:
            raise(TypeError("height must be an integer"))
        elif value < 0:
            raise(ValueError("height must be >= 0"))
        self.__height = value
