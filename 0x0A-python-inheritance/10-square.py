#!/usr/bin/python3
"""
module contains class Square inherited from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        # this creates private attribute __width, __height inherited
        # from Rectangle and set them to size:
        # __width = size, __height = size
        # so now Square has three private attributes
        super().__init__(size, size)
