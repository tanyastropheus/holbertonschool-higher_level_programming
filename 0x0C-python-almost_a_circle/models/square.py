#!/usr/bin/python3
"""Module contains class Square inherited from class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Produces a square based on given parameters."""
    def __init__(self, size, x=0, y=0, id=None):  # accepts arguments passed
        """Initializing instances of class Square.

        Args:
           width (int): width of the square.
           height (int): height of the square.
           x (int): horizontal (x-axis) offset of the square.
           y (int): vertical (y-axis) offset of the square.
           id (int): id of the Square instance.

        """
        super().__init__(size, size, x, y, id)  # calls parent with arguments

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
