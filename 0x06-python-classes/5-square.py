#!/usr/bin/python3
"""Sqaure"""


class Square:
    """Sqaure inside"""

    def __init__(self, size=0):
        """init"""
        self.__size = size

    @property
    def size(self):
        """Return"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
