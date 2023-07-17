#!/usr/bin/python3
"""
Unittest for Square class
"""
import unittest
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareClass(unittest.TestCase):
    """Test Cases for the Square class"""

    def setUp(self):
        """Set up test case"""
        self.square_instance = Square(2, 3, 4, 5)

    def tearDown(self):
        """Tear down test case"""
        del self.square_instance
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        square_dict = self.square_instance.to_dictionary()
        expected_dict = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(square_dict, expected_dict)

    def test_to_dictionary_type(self):
        """Test the type of the dictionary returned by to_dictionary"""
        square_dict = self.square_instance.to_dictionary()
        expected_dict = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(type(square_dict).__name__, type(expected_dict).__name__)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.square_instance.area(), 4)

    def test_get_set_size(self):
        """Test getting and setting size"""
        self.square_instance.size = 30
        self.assertEqual(str(self.square_instance), "[Square] (5) 3/4 - 30")

    def test_set_size_with_invalid_value(self):
        """Test setting size with invalid value"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.square_instance.size = "Fault"

    def out_stdout(self, sq=None):
        """Capture the stdout of display method"""
        t = sys.stdout
        sys.stdout = StringIO()
        if sq is None:
            self.square_instance.display()
        else:
            sq.display()
        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = t
        return output

    def test_display(self):
        """Test the display method"""
        display_output = "\n\n\n\n   ##\n   ##\n"
        output = self.out_stdout()
        self.assertEqual(output, display_output)

    def test_display_larger_square(self):
        """Test the display method with a larger square"""
        r1 = Rectangle(4, 6)
        display_output = "####\n####\n####\n####\n####\n####\n"
        output = self.out_stdout(r1)
        self.assertEqual(output, display_output)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.square_instance), "[Square] (5) 3/4 - 2")

    def test_update_with_args(self):
        """Test the update method with *args"""
        self.square_instance.update(89)
        self.assertEqual(str(self.square_instance), "[Square] (89) 3/4 - 2")

    def test_update_with_kwargs(self):
        """Test the update method with **kwargs"""
        self.square_instance.update(x=6, y=3, size=7)
        self.assertEqual(str(self.square_instance), "[Square] (5) 6/3 - 7")

    def test_id(self):
        """Test the id attribute"""
        self.assertEqual(self.square_instance.id, 5)

    def test_id_after_set(self):
        """Test the id attribute after setting a new id"""
        self.square_instance.id = 0
        sq1 = Square(1, 2)
        sq2 = Square(2, 1)
        sq3 = Square(1, 2, 3, 4)
        self.assertEqual(sq3.id, 3)

    def test_width(self):
        """Test the width (size) attribute"""
        self.assertEqual(self.square_instance.width, 2)

    def test_height(self):
        """Test the height (size) attribute"""
        self.assertEqual(self.square_instance.height, 2)

    def test_x(self):
        """Test the x attribute"""
        self.assertEqual(self.square_instance.x, 3)

    def test_y(self):
        """Test the y attribute"""
        self.assertEqual(self.square_instance.y, 4)

    def test_raise_width_typeerror(self):
        """Test raising TypeError for width (size)"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.square_instance.width = "Fault"

    def test_raise_height_typeerror(self):
        """Test raising TypeError for height (size)"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.square_instance.height = "Fault"

    def test_raise_x_typeerror(self):
        """Test raising TypeError for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.square_instance.x = "Fault"

    def test_raise_y_typeerror(self):
        """Test raising TypeError for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.square_instance.y = "Fault"

    def test_raise_width_valueerror(self):
        """Test raising ValueError for width (size)"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.square_instance.width = 0

    def test_raise_height_valueerror(self):
        """Test raising ValueError for height (size)"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.square_instance.height = 0

    def test_raise_x_valueerror(self):
        """Test raising ValueError for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.square_instance.x = -1

    def test_raise_y_valueerror(self):
        """Test raising ValueError for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.square_instance.y = -1

if __name__ == "__main__":
    unittest.main()
