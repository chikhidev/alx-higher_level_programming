#!/usr/bin/python3
"""
Defines the Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.__size = size
        super().__init__(self.__size, self.__size)