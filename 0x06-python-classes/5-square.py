#!/usr/bin/python3
"""Printing a Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Instantiation with size.

        Args:
        size: the size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates size and sets the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for num in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
