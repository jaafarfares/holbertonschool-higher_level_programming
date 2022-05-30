#!/usr/bin/python3
"""inherit  a class
from another function"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherits from 'BaseGeometry'  """
    def __init__(self, width, height):
        """the method parameter"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
