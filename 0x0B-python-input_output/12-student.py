#!/usr/bin/python3
"""contains class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a class Student instance"""
        d = self.__dict__
        new_d = {}
        if attrs is None:
            return d
        for key, value in d.items():
            if key in attrs:
                new_d[key] = value
        return new_d
