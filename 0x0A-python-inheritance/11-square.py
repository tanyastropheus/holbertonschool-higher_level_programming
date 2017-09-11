#!/usr/bin/python3
"""
module contains class Square inherited from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # no need to pass self

    # since Rectangle used self.__class__.__name__, Square calls __str__
    # from Rectangle, and interprets 'self' in context (as an instance of
    # class Rectangle)
