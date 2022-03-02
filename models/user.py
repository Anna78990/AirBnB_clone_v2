#!/usr/bin/python3
"""Define the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User:

    Attributes:
        - email (str): email of the user
        - password (str): password of the user
        - first_name (str): first name of the user
        - last_name (str): last_name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
