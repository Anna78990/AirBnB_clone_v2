#!/usr/bin/python3
"""Define a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a rewiew

    Attributes:
        - place_id (str) = id of the place
        - user_id (str) = id of the place
        - text (str) = text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
