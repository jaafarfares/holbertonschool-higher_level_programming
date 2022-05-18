#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """declare theclass"""

    def __init__(self, size=0, position=(0, 0)):
        """assgin the value"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """return the size"""
        return self.__size

    @property
    def position(self):
        """Private instance attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """raise an exceptionif its not integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """return the square"""
            self.__size = value

    @position.setter
    def position(self, value):
        """set the position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculate the Square size"""
        return self.__size ** 2

    def my_print(self):
        """print the square with special charchter"""
        if self.size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print(end="\n")
