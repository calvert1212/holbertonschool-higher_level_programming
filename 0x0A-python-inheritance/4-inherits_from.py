#!/usr/bin/python3
"""
Method by the name inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
