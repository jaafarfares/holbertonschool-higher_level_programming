#!/usr/bin/python3
"""A python program that declare a basegeometry """



class BaseGeometry:
    """the method parameter"""
    
    def integer_validator(self, name, value):
    """ assgin the value"""
        if type(value) is int:
            raise exception(name + "<name> must be an integer")
        if value <= 0:
            raise ValueError(name + "<name> must be greater than 0")

    def area(self):
        
        raise(Exception("area() is not implemented"))

