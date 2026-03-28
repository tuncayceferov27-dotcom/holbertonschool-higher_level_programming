#!/usr/bin/python3
"""
Module for custom object serialization using pickle.
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a formatted way."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of CustomObject from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None
