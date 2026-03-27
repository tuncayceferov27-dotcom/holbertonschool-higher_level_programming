#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute"""


class Square:
    """Class that defines a square"""

    def __init__(self, size):
        """
        Initialize the square.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
