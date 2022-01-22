#!/usr/bin/python3
"""
This module contains the method: append_write.
"""


def append_write(filename="", text=""):
    """
    Append writes to a file, creates one if none.
    """
    length = len(text)
    with open(filename, "a") as x:
        x.write(text)
    return length
