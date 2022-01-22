#!/usr/bin/python3
"""
This module contains the method: read_file.
"""


def read_file(filename=""):
    """
    Reads a file and prints it
    """
    with open(filename) as x:
        for line in x:
            print(line, end="")
