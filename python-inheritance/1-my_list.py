#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""

class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
