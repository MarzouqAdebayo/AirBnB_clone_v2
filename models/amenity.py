#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Amenity Defined the amenity model

    Args:
        BaseModel: inherits from BaseModel class
    """
    __tablename__ = "amenities"

    if (storage_type == 'db'):
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', back_populates="amenities",
                                       secondary=models.place.place_amenity)
    else:
        name = ""
