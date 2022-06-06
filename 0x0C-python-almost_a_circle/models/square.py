#!/usr/bin/python3
""" Square module """
from . rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                keys = kwargs.items()
                for i in keys:
                    if i == "id":
                        self.id = keys
                    if i == "size":
                        self.size = keys
                    if i == "x":
                        self.x = keys
                    if i == "y":
                        self.y = keys
