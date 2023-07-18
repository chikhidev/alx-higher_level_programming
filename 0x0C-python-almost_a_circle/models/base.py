#!/usr/bin/python3
"""
base.py module
"""
import turtle
import json
import csv


class Base:
    """
    Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): Unique identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV representation of list_objs to a file.

        Args:
            list_objs (list): List of instances to be written to the file.
        """
        csv_file = cls.__name__ + ".csv"
        fieldnames = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']

        with open(csv_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(obj.to_dictionary() for obj in list_objs) if list_objs else []

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: List of instances.
        """
        csv_file = cls.__name__ + ".csv"
        fieldnames = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']

        try:
            with open(csv_file, "r") as file:
                reader = csv.reader(file, delimiter=',')
                return [cls(**{field: int(value) for field, value in zip(fieldnames, row) if value}) for i, row in enumerate(reader) if i > 0]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        try:
            with open(str(cls.__name__) + ".json", "r") as file:
                l = cls.from_json_string(file.read())

            num_ins = len(l)
            instances = []
            for y in range(num_ins):
                instances.append(cls.create(**l[y]))

            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: Dictionary containing the instance's attributes.

        Returns:
            Base: New instance with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON representation of list_objs to a file.

        Args:
            list_objs (list): List of instances to be written to the file.
        """
        if list_objs is None or list_objs == []:
            l = []
        else:
            l = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list from the JSON string representation json_string.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List from the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw all Rectangles and Squares using the Turtle graphics module.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        #tha screen
        screen = turtle.Screen()
        screen.setup(width=800, height=600)

        #za object
        t = turtle.Turtle()
        #speed
        t.speed(1)

        #draw the rectangle
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        #draw the square
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)

        screen.exitonclick()
