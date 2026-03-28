#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle using BaseGeometry validation"""

    def __init__(self, width, height):
        """
        Initialize the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height
