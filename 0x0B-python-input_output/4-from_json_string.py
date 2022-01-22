#!/usr/bin/python3
"""
This module contains method: from_json_string.
"""
import json


def from_json_string(my_str):
    """
    This method returns an object from a JSON string.
    """
    return json.loads(my_str)
