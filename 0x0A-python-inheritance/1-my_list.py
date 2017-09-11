#!/usr/bin/python3
"""contains MyList class inherited from the list class"""


class MyList(list):
    def print_sorted(self):
        """prints a sorted copy of the list"""
        print(sorted(self))
