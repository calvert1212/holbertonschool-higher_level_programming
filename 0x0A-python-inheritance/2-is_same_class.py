#!/usr/bin/python3
"""
The method called is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Returns true if obj is instance of a_class. Else, returns false.
    """
    return (type(obj) == a_class)
