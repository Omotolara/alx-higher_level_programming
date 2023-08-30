#!/usr/bin/python3
"""Coordinates of a Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size and position.

        Args:
        size: the size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates size and sets the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position


    @position.setter
    def position(self, value):
        """Validates position and sets the value"""
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for num in range(self.__position[1]):
            print()
        for num in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        if self.__size == 0:
            print()
            return
