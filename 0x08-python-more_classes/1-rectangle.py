#!/usr/bin/python3
'''a python programe to define a rectangle'''


class Rectangle:
    '''declare the class rectangle'''
    def __init__(self, width=0, height=0):
        '''function arguments'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''a class method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''a class method'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''a class method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''a class method'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
