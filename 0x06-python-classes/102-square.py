#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square. Default value is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the square is equal
        to the area of another square.
        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if the area of the square is not
        equal to the area of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        """
        Checks if the area of the square is greater
        than the area of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of the square is greater
        than or equal to the area of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is greater than
            or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if the area of the square is less
        than the area of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of the square is less than or
        equal to the area of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is less than
            or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
