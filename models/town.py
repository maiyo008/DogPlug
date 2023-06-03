#!/usr/bin/python3
""" Town module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Town(BaseModel, Base):
    """ A representation of a Town"""
    if storage_type == "db":
        __tablename__ = "towns"
        name = Column(String(40), nullable=False, default="")
        county_id = Column(String(100), ForeignKey("counties.id"), nullable=False)
        locations = relationship(
            "Location",
            backref="town",
            cascade="all, delete, delete-orphan"
        )

    def __init__(self, *args, **kwargs):
        """ Initialization of a town object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.name = ""
            self.county_id = ""
