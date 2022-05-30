#!/usr/bin/python3
"""Write a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherits from BaseGeometry  """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
