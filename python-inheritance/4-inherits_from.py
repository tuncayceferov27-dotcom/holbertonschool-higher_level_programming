#!/usr/bin/python3
"""Function that checks if object inherits from a class (not exactly the class)"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a class that inherits from a_class"""
    return type(obj) is not a_class and isinstance(obj, a_class)
