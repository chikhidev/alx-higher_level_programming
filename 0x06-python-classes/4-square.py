#!/usr/bin/python3
"""Square"""


class Square:
    """Square inside"""

    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """get/set size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return"""
        return (self.__size * self.__size)
