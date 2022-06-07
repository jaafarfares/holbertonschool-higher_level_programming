#!/usr/bin/python3
""" base class """
import json


class Base:
    """a public object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define the method parameter"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
