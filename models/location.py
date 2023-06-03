#!/usr/bin/python3
""" Location module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey


class Location(BaseModel, Base):
    """ A representation of location"""
    if storage_type == "db":
        __tablename__ = "locations"
        longitude = Column(String(40), nullable=True, default="")
        latitude = Column(String(40), nullable=True, default="")
        groomer_id = Column(String(40), ForeignKey("groomers.id"), nullable=False)
        town_id = Column(String(40), ForeignKey("towns.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialization of a Location object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.longitude = ""
            self.latitude = ""
            self.town_id = ""
            self.county_id = ""
