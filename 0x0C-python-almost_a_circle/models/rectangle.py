#!/usr/bin/python3
"""
    rectangle.py module
"""

validate_integer_property = __import__('helpers').validate_integer_property

class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Default is 0.
            y (int, optional): y-coordinate of the rectangle's position. Default is 0.
            id (any, optional): Unique identifier for the rectangle. Default is None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: String representation of the rectangle in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        idd = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(idd, x, y, w, h)
    

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        validate_integer_property(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        validate_integer_property(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        validate_integer_property(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        validate_integer_property(y, "y")
        self.__y = y


    def display(self):
        """
        Display the rectangle with the character '#'.
        """
        if self.__height == 0 or self.__width == 0:
            return

        empty_line = ' ' * self.__x
        rectangle_line = '#' * self.__width

        for _ in range(self.__y):
            print()

        for _ in range(self.__height - 1):
            print(empty_line + rectangle_line)

        print(empty_line + rectangle_line)

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height


    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: Dictionary containing the rectangle's attributes.
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}

    def update(self, *args):
        """
        Assigns arguments to each attribute of the Rectangle.

        Args:
            *args: Variable length argument list. Can be used in the order (id, width, height, x, y).
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]