#!/usr/bin/python3
"""Module that defines a rebel class MyInt that inherits from int"""


class MyInt(int):
    """MyInt is a rebel: it has == and != operators inverted"""

    def __eq__(self, other):
        """Invert the == operator to behave like !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator to behave like =="""
        return super().__eq__(other)
