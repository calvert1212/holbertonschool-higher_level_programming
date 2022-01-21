#!/usr/bin/python3
"""
Creates class for MyList, inherits from superclass list.
"""


class MyList(list):
    """
    A subclass of the superclass "list."
    """
    def __init__(self):
        """
        Initializes the class MyList.
        """
        pass

    def print_sorted(self):
        """
        Prints the list contained in self in sorted ascending order.
        """
        print(sorted(self))
