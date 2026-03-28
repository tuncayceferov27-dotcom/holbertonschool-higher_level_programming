#!/usr/bin/python3
"""MyList module

This module defines a class MyList that inherits from list
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """Custom list class that inherits from the built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        sorted_list = sorted(self)
        print(sorted_list)
