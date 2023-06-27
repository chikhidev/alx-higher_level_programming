#!/usr/bin/python3
"""MagicClass"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return"""
        return (2 * math.pi * self.__radius)
