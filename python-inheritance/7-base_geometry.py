#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer validation"""


class BaseGeometry:
    """Class representing base geometry logic"""

    def area(self):
        """
        Public instance method that is not yet implemented.
        
        Raises:
            Exception: with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.

        Args:
            name (str): The name of the value (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
