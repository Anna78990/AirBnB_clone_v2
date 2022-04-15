#!/usr/bin/python3
""" Unittest for db_storage """

import unittest
import os
import sys
import json
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State

class Test_DBStorage(unittest.TestCase):
    """ Test class for DBStorage """

    def test_new(self):
        """ test for 'new' method """
        storage = DBStorage()
        length = len(storage.all(State).keys())
        my_state = State()
        storage.new(my_state)
        storage.save()
        length2 = len(storage.all(State).keys())
        self.assertEqual(length + 1, length2)
        storage.close()

if __name__ == "__main__":
    unittest.main()
