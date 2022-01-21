#!/usr/bin/python3
"""
Method bye the name is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if obj is instance of or descended from a_class, else false.
    """
    return isinstance(obj, (a_class))
