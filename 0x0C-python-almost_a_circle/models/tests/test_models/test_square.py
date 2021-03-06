#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import inspect


class TestSquareClass(unittest.TestCase):
    """
    The Rectangle class test class.
    """
    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len('square'.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Testing method docstrings.
        """
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.size.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)

    def test_init(self):
        """
        Testing the init method.
        """
        Square1 = Square(10, 1, 2, 5)
        self.assertEqual(Square1.id, 5)
        self.assertEqual(Square1.size, 10)
        self.assertEqual(Square1.x, 1)
        self.assertEqual(Square1.y, 2)
        # Bad args
        with self.assertRaises(TypeError):
            Square2 = Square(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            Square2 = Square()
        # Bad size
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square2 = Square("ten", 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square2 = Square(10.5, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square2 = Square([], 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square2 = Square({}, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square2 = Square(-10, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square2 = Square(0, 1, 2, 5)
        # Bad x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square2 = Square(10, "one", 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square2 = Square(10, 1.5, 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square2 = Square(10, [], 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square2 = Square(10, {}, 2, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square2 = Square(10, -1, 2, 5)
        # Bad y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square2 = Square(10, 1, "two", 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square2 = Square(10, 1, 2.5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square2 = Square(10, 1, [], 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square2 = Square(10, 1, {}, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square2 = Square(10, 1, -2, 5)

    def test_size_setter(self):
        """
        Testing the setter for Square size.
        """
        Square1 = Square(10, 1, 2, 5)
        self.assertEqual(Square1.size, 10)
        Square1.size = 20
        self.assertEqual(Square1.size, 20)
        # Bad values/types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square1.size = "twenty"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square1.size = 20.5
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square1.size = []
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square1.size = {}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square1.size = -20
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square1.size = 0

    def test_update(self):
        """
        Testing the update method.
        """
        Square1 = Square(10, 1, 2, 5)
        # Using args
        Square1.update(10, 20, 2, 3)
        self.assertEqual(Square1.id, 10)
        self.assertEqual(Square1.size, 20)
        self.assertEqual(Square1.x, 2)
        self.assertEqual(Square1.y, 3)
        # Using kwargs
        Square1.update(size=30, id=20, x=3, y=4)
        self.assertEqual(Square1.size, 30)
        self.assertEqual(Square1.id, 20)
        self.assertEqual(Square1.x, 3)
        self.assertEqual(Square1.y, 4)

    def test_to_dictionary(self):
        """
        Testing the to_dictionary method.
        """
        Square1 = Square(10, 1, 2, 5)
        Square1_dict = Square1.to_dictionary()
        self.assertTrue(type(Square1_dict) is dict)
        dict1 = {'id': 5, 'size': 10, 'x': 1, 'y': 2}
        self.assertEqual(Square1_dict, dict1)

if __name__ == "__main__":
    unittest.main()
