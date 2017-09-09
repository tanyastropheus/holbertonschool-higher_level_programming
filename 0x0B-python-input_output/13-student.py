#!/usr/bin/python3
"""contains class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a class Student instance

        Args:
            attrs (list): list of writable attributes; the writable attributes
        of a class Student instance is modified by the attrs list


        Returns:
            dictionary representation of writable attributes contains in the
        attrs list, or all writable attributes if attres is None

        """
        return {k: v for k, v in self.__dict__.items()
                if not attrs or k in attrs}

    def reload_from_json(self, json):
        """modifies writable attributes in Student instance based on JSON
        dictionary representation

        """
        self.__dict__ = {k: v for k, v in json.items()}
