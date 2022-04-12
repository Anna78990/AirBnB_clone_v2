#!/usr/bin/python3
"""Define the class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a User:

    Attributes:
        - email (str): email of the user
        - password (str): password of the user
        - first_name (str): first name of the user
        - last_name (str): last_name of the user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
