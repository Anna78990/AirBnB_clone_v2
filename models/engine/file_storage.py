#!/usr/bin/python3
"""Define a class FileStorage to store information"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represents a Filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return dictionary __objects"""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for (key, obj) in self.__objects.items()
                    if isinstance(obj, cls)}

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            sobj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(sobj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                list_obj = json.load(f)
                for o in list_obj.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete the object"""
        if (obj is not None):
            for k in self.__objects.keys():
                if self.__objects[k] == obj:
                    stk = k
            self.__objects.pop(stk)

    def close(self):
        """ call reload method """
        self.reload()
