#!/usr/bin/python3
"""Define a class FileStorage to store information"""
import json


class FileStorage:
    """Represents a Filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
