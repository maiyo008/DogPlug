#!/usr/bin/python3
""" Location module """
from models.base_model import BaseModel


class Location(BaseModel):
    """ A representation of location"""

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
