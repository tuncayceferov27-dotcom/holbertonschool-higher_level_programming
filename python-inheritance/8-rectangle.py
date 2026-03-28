#!/usr/bin/python3
"""Rectangle module that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes (name mangling)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
