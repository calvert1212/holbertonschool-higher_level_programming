#!/usr/bin/python3
"""
Second iteration of the Rectangle class.
"""


class Rectangle:
    """
    Defines a Rectangle object based on the width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Method to initialize the rectangle object.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Gets the rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle's area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle's perimeter.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
