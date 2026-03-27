#!/usr/bin/python3
"""Module that defines a Square class with an area method"""


class Square:
    """Class that defines a square by its size and can compute its area"""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): The size of the side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
