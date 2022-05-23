#!/usr/bin/python3
"""a python program that defines a rectangle"""


class Rectangle():
    number_of_instances = 0
    """ empty class rectangle"""
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """return the rectangle perimiter"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return 2*(self.__height + self.__width)

    def __str__(self):
        """ print the rectangle area with the charchter '#' """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join('#' * self.width for _ in range(self.height))

    def __repr__(self):
        """ using the repr method"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        """print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
