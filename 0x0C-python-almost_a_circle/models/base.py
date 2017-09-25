#!/usr/bin/python3
"""Module contains class Base

"""
import json

class Base:
    """Base class for classes of other shapes."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries != None:
            return json.dumps(list_dictionaries)
        return "[]"
