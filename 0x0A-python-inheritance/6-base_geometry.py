#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base class for representing geometric shapes."""

    def area(self):
        """Calculate the area of the geometric shape.

        This method is not implemented in the base class and should be overridden in derived classes to provide
        specific implementations.

        Raises:
            Exception: This method should be overridden in the derived class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
