#!/usr/bin/python3
"""a python programe that define a rectangle"""


class Rectangle:
    """declare the class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """assgin the function arguments"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """assgin the function arguments"""
        return self.__width

    @width.setter
    def width(self, value):
        """assgin the function arguments"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """assgin the function arguments"""
        return self.__height

    @height.setter
    def height(self, value):
        """assgin the function arguments"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """assgin the function arguments"""
        return self.__width * self.__height

    def perimeter(self):
        """assgin the function arguments"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """assgin the function arguments"""
        if self.__width == 0 or self.__height == 0:
            return ""
        seq = ""
        for i in range(self.__height):
            seq += "#" * self.__width
            if i != self.__height - 1:
                seq += "\n"
        return seq

    def __repr__(self):
        """assgin the function arguments"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """assgin the function arguments"""
        print("Bye rectangle...")

    def __del__(self):
        """assgin the function arguments"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
