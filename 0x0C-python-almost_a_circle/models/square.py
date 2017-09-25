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

    def update(self, *args, **kwargs):
        """updates attributes with variable number of arguments.

        Note:
           1st arg => id attribute.
           2nd arg => size attribute.
           3rd arg => x attribute.
           4th arg => y attribute.

        """

        attrs = ['id', 'size', 'x', 'y']

        if args:
            for i in range(min(len(attrs), len(args))):
                setattr(self, attrs[i], args[i])
                # setattr() calls setters automatically to validate value
        else:
            for k, v in kwargs.items():
                for i in attrs:
                    if k == i:
                        setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        attrs = ['id', 'size', 'x', 'y']
        return {k: getattr(self, k) for k in attrs}
