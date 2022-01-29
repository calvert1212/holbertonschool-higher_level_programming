#!/usr/bin/python3
"""
This will create the Square subclass.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square subclass inherits from Rectangle.
    Properties are defined by size, x and y.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square with attributes of superclass.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets Square size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets Square size, checks valid width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns string representation of the Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to the Square,
        else uses 'kwargs'.
        """
        attrnum = 0
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[attrnum], arg)
                attrnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary of the attributes of
        the Square.
        """
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
