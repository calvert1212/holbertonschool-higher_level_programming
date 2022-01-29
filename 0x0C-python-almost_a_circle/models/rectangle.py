#!/usr/bin/python3
"""
This file contains the Rectangle subclass.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle inherits from the Base superclass, and
    is defined by the attributeswidth, height, x, and y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle object. The id is
        inherited from the Basesuperclass.
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """
        Gets the Rectangle width.
        """
        return self.__width

    @property
    def height(self):
        """
        Gets the Rectangle height.
        """
        return self.__height

    @property
    def x(self):
        """
        Gets the Rectangle x value.
        """
        return self.__x

    @property
    def y(self):
        """
        Gets the Rectangle y value.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets the Rectangle width value.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the Rectangle height value.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the Rectangle x value.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the Rectangle y value.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the Rectangle's area value.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle to stdout with # characters.
        """
        for lines in range(self.__y):
            print()
        for row in range(self.__height):
            for spot in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the
        Rectangle object.
        """
        return "[Rectangle] \
({}) {}/{} - {}/{}".format(self.id, self.__x,
                           self.__y, self.__width,
                           self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns argument values to id, width, height, x, and y.
        If none provided, 'kwargs' will be used.
        """
        attrnum = 0
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[attrnum], arg)
                attrnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of
        the Rectangle object.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
