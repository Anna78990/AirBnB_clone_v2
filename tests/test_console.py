#!/usr/bin/python3
""" Unittest for class City """
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.city import City
from models.state import State
console = __import__('console').HBNBCommand


class TestFileStorage(unittest.TestCase):
    """
    Test of console
    """

    def test_console(self):
        """
        testing name type for class City
        """
        con = console()
        arg = 'State name="Arizona"'
        con.do_create(arg)
        with open('file.json') as f:
            contents = f.read()
        f.close()
        bool = '"name": "Arizona"' in contents
        message = "Test value is not true."
        self.assertTrue(bool, message)


if __name__ == "__main__":
    unittest.main()
