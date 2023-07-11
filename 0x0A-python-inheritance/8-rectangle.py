#!/usr/bin/python3
'''
    Implementing a Rectangle class that inherits from BaseGeometry
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Represents a rectangle.

        Attributes:
            __width (int): The width of the rectangle.
            __height (int): The height of the rectangle.
    '''
    def __init__(self, width, height):
        '''
            Initialize a Rectangle instance.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.

            Raises:
                TypeError: If width or height is not an integer.
                ValueError: If width or height is less than or equal to 0.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height