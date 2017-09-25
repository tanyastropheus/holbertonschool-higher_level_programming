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
        """returns the JSON string representation of list_dictionaries.

        Args:
           list_dictioanries (list): list of dictionaries.

        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
           list_objs (list): list of instances of classes inheriting from Base.

        """
        with open("{}.json".format(cls.__name__), 'w') as f:
            if list_objs is not None:
                # create a list of dict representation of
                # each instance from list_objs
                list_dict = [i.to_dictionary() for i in list_objs]
                # create JSON string representation of the list of dictionaries
                f.write(cls.to_json_string(list_dict))
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation.

        Args:
           json_string (list): list of JSON string representation.

        """
        # not json_string -> check if it's empty
        if not json_string or json_string is None:
            return []  # return an empty list, not a string represntn of list
        return json.loads(json_string)
