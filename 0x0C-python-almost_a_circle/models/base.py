#!/usr/bin/python3
""" base class """
from os import path
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """ loads a list of intances from a json file """
        list1 = []
        file = cls.__name__ + ".json"
        if os.path.isfile(file):
            with open(file, 'r') as f:
                res = cls.from_json_string(f.read())
                for i in res:
                    list1.append(cls.create(**i))
        return list1

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the CSV string representation of list_objs to a file
        """
        with open(cls.__name__ + ".csv", "w", newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fld = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fld = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fld)
            writer.writeheader()
            if list_objs is not None:
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load from file csv """
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", "r", newline='') as csvfile:
            list2 = []
            reader = csv.DictReader(csvfile)
            for i in reader:
                for key, value in i.items():
                    i[key] = int(value)
                list2.append(cls(**i))
        return list2
