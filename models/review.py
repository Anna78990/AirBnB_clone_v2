#!/usr/bin/python3
"""Define a class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represent a rewiew

    Attributes:
        - place_id (str) = id of the place
        - user_id (str) = id of the place
        - text (str) = text of the review
    """

    place_id = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    text = Column(String(60), ForeignKey("users.id"), nullable=False)
