#!/usr/bin/python3
"""Module contains class Rectangle inherited from class Base

"""

from models.base import Base


class Rectangle(Base):
    """Produces a rectangle based on given parameters.

    """

    def __init__(self, width, height, x=0, y=0, id=None):  # accepts parameters
        """Initializing instances of class Rectangle.

        Args:
           width (int): width of the rectangle.
           height (int): height of the rectangle.
           x (int): horizontal (x-axis) offset of the rectangle.
           y (int): vertical (y-axis) offset of the rectangle.
           id (int): id of the Rectangle instance.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # calling the parent's init by passing id

    def validator(self, name, value):
        """validates private attributes initiated in __init__.

        Args:
           name (str): name of the attribute.
           value (int): value to be validated for the named attribute.

        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        """retrieves and sets private attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """retrieves and sets private attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """retrieves and sets private attribute __x."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """retrieves and sets private attribute __y."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        # output of print() is sent to stdout (sys.stdout) by default
        for a in range(self.y):
            print()
        for i in range(self.height):
            for j in range(1):
                print(' ' * self.x, end="")
                print('#' * self.width, end="")
            print()

    def __str__(self):  # overloading: overriding __str__ from parent class
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args):
        """updates attributes with variable number of arguments.

        Note:
           1st arg => id attribute.
           2nd arg => width attribute.
           3rd arg => height attribute.
           4th arg => x attribute.
           5th arg => y attribute.

        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(min(len(attrs), len(args))):
            setattr(self, attrs[i], args[i])  # setattr() calls setters automatically to validate value
