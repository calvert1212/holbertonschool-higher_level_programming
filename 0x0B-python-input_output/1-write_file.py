#!/usr/bin/python3
"""
This module contains the method: write_file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a file, creates one if none, overwrites.
    """
    length = len(text)
    with open(filename, "w") as x:
        x.write(text)
    return length
