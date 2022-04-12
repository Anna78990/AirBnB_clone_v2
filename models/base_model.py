#!/usr/bin/python3
""" Defines the BaseModel class """
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """Represents the BaseModel class"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

            Args:
                - *args : unused
                - **kwargs : key/value
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Return a representation of a BaseModel instance in a string"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        if dict["_sa_instance_state"]:
            del dict["_sa_instance_state"]
        return dict

    def delete(self):
        """ Delete the current instance from the storage"""
        models.storage.delete(self)
