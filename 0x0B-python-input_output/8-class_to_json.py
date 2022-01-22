#!/usr/bin/python3
"""
This module contains the method: class_to_json.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of the
    JSON serialization of a class.
    """
    return obj.__dict__
