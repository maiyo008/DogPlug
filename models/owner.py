#!/usr/bin/python3
""" Owner module"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Owner(BaseModel, Base):
    """ Representation of an owner"""
    if storage_type == "db":
        __tablename__ = "owners"
        name = Column(String(100), nullable=False, default="")
        email = Column(String(40), nullable=False, default="name@gmail.com")
        contact = Column(String(20), nullable=False, default="")
        dogs = relationship(
            "Dog",
            backref="owner",
            cascade="all, delete, delete-orphan"
        )
        reviews = relationship(
            "Review",
            backref="owner",
            cascade="all, delete, delete-orphan"
        )

    def __init__(self, *args, **kwargs):
        """ Initialize an Owner """
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.name = ""
            self.email = ""
            self.contact = ""
            self.dog_id = ""
            self.location_id =""
