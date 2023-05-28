#!/usr/bin/python3
""" Town module """
from models.base_model import BaseModel


class Town(BaseModel):
    """ A representation of a Town"""

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
