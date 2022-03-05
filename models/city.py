#!/usr/bin/python3
"""Define a class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city

    Attributes:
        - state_id (str): id of the state
        - name (str): name of the city
    """

    state_id = ""
    name = ""
