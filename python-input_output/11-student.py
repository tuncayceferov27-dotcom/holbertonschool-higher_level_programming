#!/usr/bin/python3
"""Module that defines a Student class with serialization and deserialization"""


class Student:
    """Class that defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in this
        list are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and \
           all(isinstance(item, str) for item in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
