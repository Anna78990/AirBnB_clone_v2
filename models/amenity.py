#!/usr/bin/python3
"""Define a class Amenity"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity

    Attribute:
        - name (str): name of the amenity(column)
        - __tablename__ (table): represents the table name, amenities
        - place_amenities (relationship): relationship between
                                          place and amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", back_populates="amenities")
