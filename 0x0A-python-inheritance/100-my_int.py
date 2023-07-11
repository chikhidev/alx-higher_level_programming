#!/usr/bin/python3
"""Defines the MyInt class that inherits from int."""


class MyInt(int):
    """
    Represents a custom integer class with inverted comparison operators.

    This class inherits from the built-in int class and overrides the equality (__eq__)
    and inequality (__ne__) operators to invert their behavior.

    Methods:
        __eq__(self, value): Override == operator with != behavior.
        __ne__(self, value): Override != operator with == behavior.
    """

    def __eq__(self, value):
        """
        Override the equality (==) operator with inequality (!=) behavior.

        Args:
            value: The value to compare against.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override the inequality (!=) operator with equality (==) behavior.

        Args:
            value: The value to compare against.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real == value