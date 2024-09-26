#!/usr/bin/python3
<<<<<<< HEAD
""" Amenity Module for HBNB project """

=======
"""This is the amenity class"""
>>>>>>> parent of 06df725 (models)
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """ Amenity class """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity', viewonly=False)
=======
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
>>>>>>> parent of 06df725 (models)
