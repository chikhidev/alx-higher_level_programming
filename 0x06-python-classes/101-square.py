#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

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

    @property
    def position(self):
        """Returns the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (int, int): The position value to set.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print("")

    def __str__(self):
        """Returns the string representation of the square."""
        if self.__size != 0:
            [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            if _ != self.__size - 1:
                print("")
        return ""
