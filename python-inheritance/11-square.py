#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square based on Rectangle"""

    def __init__(self, size):
        """
        Initialize the Square.

        Args:
            size (int): The size of the square's side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description in [Square] <width>/<height> format"""
        return "[Square] {}/{}".format(self.__size, self.__size)
