#!/usr/bin/python3
"""A Magic Class that performs a bytecode operation"""

import math


class MagicClass:
    """Defines a circle."""

    def __init__(self, radius=0):
        """Instantiation of a circle.

        Arg:
            radius: the radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the circle"""
        return (2 * math.pi * self.__radius)
