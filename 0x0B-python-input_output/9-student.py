#!/usr/bin/python3
"""
This module contains the class: Student.
"""


class Student:
    """
    Creates a Student object with parameters first, last, age.
    """
    def __init__(self, first_name, last_name, age):
        """
        This method initializes the object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of
        itself.
        """
        return self.__dict__
