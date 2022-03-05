#!/usr/bin/python3
""" test class FileStorage """
import unittest
import os
import sys
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class FileStorage """

    def test_all(self):
        """ test return type of method all """
        storage = FileStorage()
        test_type = storage.all()
        self.assertEqual(type(test_type), dict)

    def test_new(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        key = str(my_model.__class__.__name__ + "." + my_model.id)
        self.assertTrue(key in storage._FileStorage__objects)

    def test_save_exist_file(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_read_json(self):
        storage = FileStorage()
        storage.save()

        with open("file.json", 'r') as json_file:
            content = json.load(json_file)

        self.assertTrue(type(content), dict)

    def test_reaload_without_file(self):
        storage = FileStorage()
        try:
            storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
