#!/usr/bin/python3
class Rectangle:
    """A class that defines a rectangle by the given width and height"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves and sets private attribute __width for the Rectangle class

        raises:
            TypeError: if __width is not an integer
            ValueError: if __width is less than 0

        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves private attribute __height for the Rectangle class

        raises:
            TypeError: if __width is not an integer
            ValueError: if __width is less than 0

        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Function that calculates the area of the rectangle

        Returns:
            area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Function that calculates the perimeter of the rectangle

        if the width or height is zero, the perimeter equals to zero

        Returns:
            perimeter of the rectangle.

        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        line = "".join(str(self.print_symbol) * self.__width + '\n')
        return "{}".format(line * self.__height, end="")

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
