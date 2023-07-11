#!/usr/bin/python3
"""Defines the BaseGeometry class for representing geometric shapes."""


class BaseGeometry:
    """Base class for representing geometric shapes."""


    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Calculate the area of the geometric shape.

        This method is not implemented in the base class and should be overridden in derived classes to provide
        specific implementations.

        Raises:
            Exception: This method should be overridden in the derived class.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
