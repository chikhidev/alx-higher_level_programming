#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Set up test case"""
        self.inst = Base(5)

    def tearDown(self):
        """Tear down test case"""
        Base._Base__nb_objects = 0

    def test_nb_objects_default(self):
        """Test the default value of __nb_objects"""
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_nb_objects_increment(self):
        """Test the increment of __nb_objects when creating a new instance"""
        self.inst = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_id(self):
        """Test the id attribute of the instance"""
        self.assertEqual(self.inst.id, 5)

if __name__ == "__main__":
    unittest.main()
