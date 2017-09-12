#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):  # accepts parameters
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # calling the parent's init by passing id

    def validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def area(self):
        # what if x, y are not zero?
        return self.width * self.height

    def display(self):
        # output of print() is sent to stdout (sys.stdout) by default
        for i in range(self.width):
            for j in range(self.height):
                print('#', end="")
            print()
