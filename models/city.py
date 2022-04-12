#!/usr/bin/python3
"""Define a class city"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Represent a city

    Attributes:
        - __tablename__ (str): name of the MySql table
        - state_id (str): id of the state
        - name (str): name of the city
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    places = relationship("Place", backref="cities", cascade="delete")
