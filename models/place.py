#!/usr/bin/python3
"""Define a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
import models
from models.review import Review
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """Represent a place

    Attributes:
        - __tablename__ (str): name of the MySql table
        - city_id (str): id of the city
        - user_id (str): id of the user
        - name (str): name of the state
        - description (str): description of the place
        - number_rooms (int): number of rooms
        - number_bathrooms (int): number of bathrooms
        - max_guest (int): max guest
        - price_by_night (int): price by night
        - latitude (float): latitude of the place
        - longitude (float): longitude of the place
        - amenity_ids (list): list of amenity's ids
        - reviews (relationship): relationship between Place and Review classes
        - amenities (relationship): relationship between Amenity,
                                    place_amenity and places
        """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False)

    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 nullable=False, primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 nullable=False, primary_key=True))

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Getter in case of file storage """
            return [review for review in models.storage.all(Review)
                    if review.state_id == self.id]

        @property
        def amenities(self):
            """ Getter in case of file storage """
            return [amenity for amenity in models.storage.all(Amenity)
                    if amenity.id in self.amenity_ids]

        @amenities.getter
        def amenities(self, obj):
            """ Setter in case of file storage"""
            if type(obj) == Amenity():
                self.amenity_ids.append(obj)
