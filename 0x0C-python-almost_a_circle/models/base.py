#!/usr/bin/python3
"""
This file represents the Base superclass.
"""
import json
import os


class Base:
    """
    This superclass is the basis for its subclasses. Each subclass
    has a unique id utilizing private attribute nb_objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base object.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of
        a dictionary.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of an
        object to a file.
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an object with the attributes set by
        kwargs.
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances of a particular
        class.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            newlist = cls.from_json_string(file.read())
        newobj = []
        for dict in newlist:
            newobj.append(cls.create(**dict))
        return newobj
