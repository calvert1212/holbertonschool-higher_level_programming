#!/usr/bin/python3
"""
This module contains the method: load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    This creates an object from a JSON file.
    """
    with open(filename) as x:
        return json.load(x)
