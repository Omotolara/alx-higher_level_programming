#!/usr/bin/python3
"""Square with size"""


class Square:
    """Defines a square"""

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def __init__(self, size=0):
        """Instantiation with size.

        Args:
        size: the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
