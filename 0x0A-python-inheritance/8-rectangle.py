#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""module contains class Rectangle inherited from class BaseGeometry"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if type(width) == int and width > 0:
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if type(height) == int and height > 0:
            self.__height = height
        else:
            raise TypeError("height must be an integer")
