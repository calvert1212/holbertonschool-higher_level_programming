#!/usr/bin/python3
"""
Function to add two integers
"""


def add_integer(a, b=98):
    """
    Function that adds two given integers. If float is passed, it is cast to an
    integer.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return (a + b)
