#!/usr/bin/python3
"""Define a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class Place(BaseModel, Base):
    """Represent a place

    Attributes:
        - __tablenames__ (str): name of the MySql table
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
        """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    amenities = relationship("Amenity", back_populates="place_amenities")

    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
        Column(
            "place_id", String(60), ForeignKey("places.id"),
            nullable=False, primary_key=True
            ),
        Column(
            "amenity_id", String(60), ForeignKey("amenities.id"),
            nullable=False, primary_key=True
            )
            )

    def amenities(self):
        return amenities

    def amenities(self, amenities):
        if isinstance(Amenity, amenities):
            amenity_ids.append(amenities)
        else:
            continue

