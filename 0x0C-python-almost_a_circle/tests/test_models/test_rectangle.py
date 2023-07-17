#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Test Cases for the Rectangle class"""

    def setUp(self):
        """Set up test case"""
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def tearDown(self):
        """Tear down test case"""
        del self.inst
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r1, exp)

    def test_to_dictionary_type(self):
        """Test the type of the dictionary returned by to_dictionary"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(type(r1).__name__, type(exp).__name__)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.inst.area(), 2)

    def out_stdout(self, x=None):
        """Capture the stdout of display method"""
        t = sys.stdout
        sys.stdout = StringIO()
        if x is None:
            self.inst.display()
        else:
            x.display()
        o = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = t
        return o

    def test_display(self):
        """Test the display method"""
        display_output = "\n\n\n\n   #\n   #\n"
        o = self.out_stdout()
        self.assertEqual(o, display_output)

    def test_display_larger_rectangle(self):
        """Test the display method with a larger rectangle"""
        r1 = Rectangle(4, 6)
        display_output = "####\n####\n####\n####\n####\n####\n"
        o = self.out_stdout(r1)
        self.assertEqual(o, display_output)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.inst), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_with_args(self):
        """Test the update method with *args"""
        self.inst.update(89)
        self.assertEqual(str(self.inst), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_with_kwargs(self):
        """Test the update method with **kwargs"""
        self.inst.update(x=6, height=8, y=3, width=7)
        self.assertEqual(str(self.inst), "[Rectangle] (5) 6/3 - 7/8")

    def test_id(self):
        """Test the id attribute"""
        self.assertEqual(self.inst.id, 5)

    def test_id_after_set(self):
        """Test the id attribute after setting a new id"""
        self.inst.id = 0
        inst1 = Rectangle(1, 2)
        inst2 = Rectangle(2, 1)
        inst3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(inst3.id, 3)

    def test_width(self):
        """Test the width attribute"""
        self.assertEqual(self.inst.width, 1)

    def test_height(self):
        """Test the height attribute"""
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """Test the x attribute"""
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """Test the y attribute"""
        self.assertEqual(self.inst.y, 4)

    def test_raise_width_typeerror(self):
        """Test raising TypeError for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.width = "Fault"

    def test_raise_height_typeerror(self):
        """Test raising TypeError for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.inst.height = "Fault"

    def test_raise_x_typeerror(self):
        """Test raising TypeError for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.inst.x = "Fault"

    def test_raise_y_typeerror(self):
        """Test raising TypeError for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.inst.y = "Fault"

    def test_raise_width_valueerror(self):
        """Test raising ValueError for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.inst.width = 0

    def test_raise_height_valueerror(self):
        """Test raising ValueError for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.inst.height = 0

    def test_raise_x_valueerror(self):
        """Test raising ValueError for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.inst.x = -1

    def test_raise_y_valueerror(self):
        """Test raising ValueError for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.inst.y = -1

if __name__ == "__main__":
    unittest.main()
