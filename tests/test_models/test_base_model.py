#!/usr/bin/python3
""" Unittest of Base class"""

import unittest
from models.base_model import Base

class TestBaseModel(unittest.TestCase):
    """ Test of class Base """

    def test_id(self):
        """test method for id of BaseModel
        """
        b = BaseModel()
        self.assertEqual(type(b.id), type("abc")

    def test_method_created_at(self):
        """test method for created_at of base
        """
        b = BaseModel()
        d = datetime.now()
        self.assertEqual(str(b.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_method_updated_at(self):
        """test method for updated_at of base
        """
        b = BaseModel()

    def test_save_to_file2(self):
        """test method save to file
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            f = file.read()
        self.assertEqual(f, "[]")

    def test_save_to_file2(self):
        """test method save to file
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            f = file.read()
        self.assertEqual(f, "[]")

if __name__ == "__main__":
    unittest.main()
