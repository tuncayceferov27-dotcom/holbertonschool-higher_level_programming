#!/usr/bin/python3

class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        # Private instance attribute
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
