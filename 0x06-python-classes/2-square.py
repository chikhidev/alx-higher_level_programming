#!/usr/bin/python3

"""Square class"""


class Square:
    """Squaare inside"""

    def __init__(self, size=0):
        """init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
