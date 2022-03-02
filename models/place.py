#!/usr/bin/python3
"""Define a class Place"""
from base_model import BaseModel


class Place(BaseModel):
    """Represent a place

    Attributes:
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

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
