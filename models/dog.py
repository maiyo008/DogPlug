#!/usr/bin/python3
""" Dog module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, ForeignKey


class Dog(BaseModel, Base):
    """ A representation of a dog """
    if storage_type == "db":
        __tablename__ = "dogs"
        name = Column(String(40), nullable=False, default="")
        breed = Column(String(40), nullable=False, default="")
        weight = Column(Integer, nullable=False, default=0)
        age = Column(Integer, nullable=False, default=0)
        owner_id = Column(String(40), ForeignKey("owners.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialize a dog object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.name = ""
            self.breed = ""
            self.weight = 0
            self.age = 0            
