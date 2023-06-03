#!/usr/bin/python3
""" Groomer module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Groomer(BaseModel, Base):
    """ A representation of a groomer"""
    if storage_type == "db":
        __tablename__ = "groomers"
        name = Column(String(100), nullable=False, default="")
        email= Column(String(30), nullable=False, default="name@gmail.com")
        contact = Column(String(30), nullable=False, default="")
        services = relationship(
            "Service",
            backref="groomer",
            cascade="all, delete, delete-orphan"
        )
        reviews = relationship(
            "Review",
            backref="groomer",
            cascade="all, delete, delete-orphan"
        )
        locations = relationship(
            "Location",
            backref="groomer",
            cascade="all, delete, delete-orphan"
        )

    def __init__(self, *args, **kwargs):
        """ Initialization of a groomer object"""
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
            self.service_id = ""
            self.review_id = ""
            self.location_id = ""
