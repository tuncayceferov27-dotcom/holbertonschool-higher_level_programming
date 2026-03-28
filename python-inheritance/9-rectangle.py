#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize the Rectangle and validate attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description in a specific format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
