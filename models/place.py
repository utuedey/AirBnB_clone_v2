#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
from models.city import City
#from models.amenity import Amenity
from models.review import Review
import models

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),                                 
                                 primary_key=True, nullable=False))



class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False,
                          default=0)
    number_bathrooms = Column(Integer, nullable=False,
                              default=0)
    max_guest = Column(Integer, nullable=False,
                       default=0)
    price_by_night = Column(Integer, nullable=False,
                            default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    am_id = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """Returns the instances"""
            _inst = []
            for am in am_id:
                if am.id == self.id:
                    _inst.append(am)
            return _inst

        @amenities.setter
        def amenities(self, am):
            """Adds an Amenity"""
            if type(am).__name__ == 'Amenity':
                self.am_id.append(am)
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            _rev = []
            for review in self.reviews:
                if review.place_id == self.id:
                    _rev.append(review)
            return(_rev)
        amenities = relationship("Amenity",
                                 secondary=place_amenity)
