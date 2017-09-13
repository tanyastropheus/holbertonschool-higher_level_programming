#!/usr/bin/python3
"""Module contains class Square inherited from class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Produces a square based on given parameters."""
    def __init__(self, size, x=0, y=0, id=None):  # accepts arguments passed
        """Initializing instances of class Rectangle.

        Args:
           width (int): width of the rectangle.
           height (int): height of the rectangle.
           x (int): horizontal (x-axis) offset of the rectangle.
           y (int): vertical (y-axis) offset of the rectangle.
           id (int): id of the Rectangle instance.

        """
        super().__init__(size, size, x, y, id)  # calls parent with arguments

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
