#!/usr/bin/python3
"""Module that defines a class MyList inheriting from list"""


class MyList(list):
    """A subclass of list with an additional sorting print method"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
