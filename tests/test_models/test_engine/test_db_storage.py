#!/usr/bin/python3
""" Unittest for db_storage """

import unittest
import os
import sys
import json
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel


class Test_DBStorage(unittest.TestCase):
    """ Test class for DBStorage """

    def test_all(self):
        """ test for 'all' method """
        storage = DBStorage()
        test_type = storage.all()
        self.assertEqual(type(test_type), dict)

    def test_new(self):
        """ test for 'new' method """
        my_model = BaseModel()
        storage = DBStorage()
        storage.new(my_model)
        key = str(my_model.__class__.__name__ + "." + my_model.id)
        self.assertTrue(key in storage._DBStorage__objects)

    def test_save(self):
        """ test for 'save' method """
        storage = DBStorage()
        my_model = BaseModel()
        result = storage.save(my_model)
        self.assertFalse(result == None)

    def test_delete(self):
        """ test for 'delete' method """
        storage = DBStorage()
        my_model = BaseModel()
        result = storage.delete(my_model)
        self.assertTrue(result == None)

    def test_reaload_without_file(self):
        """ test for 'reload' method """
        storage = DBStorage()
        try:
            storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_close(self):
        """ test for 'close' method """
        storage = DBStorage()
        response = storage.close()
        self.assertTrue(response)

if __name__ == "__main__":
    unittest.main()
