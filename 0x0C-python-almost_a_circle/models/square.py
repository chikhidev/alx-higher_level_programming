#!/usr/bin/python3
"""
square.py module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, a subclass of Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square's sides.
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): Unique identifier for the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: String representation of the square in the format [Square] (<id>) <x>/<y> - <size>.
        """
        idd = self.id
        x = super().x
        y = super().y
        size = super().width
        return "[Square] ({}) {}/{} - {}".format(idd, x, y, size)


    @property
    def size(self):
        """
        Get the size of the Square.

        Returns:
            int: The size of the square's sides.
        """
        return super().width

    @size.setter
    def size(self, size):
        """
        Set the size of the Square.

        Args:
            size (int): The new size for the square's sides.
        """
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)


    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: Dictionary containing the square's attributes.
        """
        return {'x': super().x, 'y': super().y, 'id': self.id, 'size': super().width}


    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute of the Square.

        Args:
            *args: Variable length argument list. Can be used in the order (id, size, x, y).
            **kwargs: Variable length keyword argument list. Can include 'id', 'size', 'x', and 'y'.
        """
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    super(Square, type(self)).width.fset(self, arg)
                    super(Square, type(self)).height.fset(self, arg)
                elif num == 2:
                    super(Square, type(self)).x.fset(self, arg)
                elif num == 3:
                    super(Square, type(self)).y.fset(self, arg)
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.fset(self, kwargs["size"])
                super(Square, type(self)).height.fset(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.fset(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.fset(self, kwargs["y"])
