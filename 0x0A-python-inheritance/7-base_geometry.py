#!/usr/bin/python3
"""module contains class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value from argument

        Args:
            name (str): name of the value
            value (int): positive integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{%s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{%s} must be greater than 0".format(name))
