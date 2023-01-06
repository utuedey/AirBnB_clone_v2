#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models


Base = declarative_base()


class BaseModel:
   """A base class for all hbnb models"""
   id = Column(String(60),
               primary_key=True,
               nullable=False)
   def __init__(self, *args, **kwargs):
       """Instatntiates a new model"""
       if kwargs:
               for key, value in kwargs.items():
                   if key == "created_at" or key == "updated_at":
                       value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                   if key != "__class__" and hasattr(self, key):
                       setattr(self, key, value)
               if self.id is None:
                   setattr(self, 'id', str(uuid.uuid4()))
               time = datetime.now()
               if self.created_at is None:
                   self.created_at = time
               if self.updated_at is None:
                   self.updated_at = time
       else:
           self.id = str(uuid.uuid4())
           self.created_at = self.updated_at = datetime.now()
   def __str__(self):
       """Returns a string representation of the instance"""
       return '[{}] ({}) {}'.format
           type(self).__name__, self.id, self.to_dict)
   def __repr__(self):
        """Return a string representaion"""
        return self.__str__(
   def save(self):
       """Updates updated_at with current time when instance is changed"""
       self.updated_at = datetime.now()
       models.storage.new(self)
       models.storage.save()
   def delete(self):
       """delete the current instance"""
       models.storage.delete(self)
   def to_dict(self):
       """Convert instance into dict format"""
       dictionary = dict(self.__dict__)
       dictionary["__class__"] = str(type(self).__name__)
       dictionary["created_at"] = self.created_at.isoformat()
       dictionary["updated_at"] = self.updated_at.isoformat()
       if "_sa_instance_state" in dictionary:
           del(dictionary['_sa_instance_state'])
       return dictionary
