#!/usr/bin/python3
""" Owner module"""
from models.base_model import BaseModel


class Owner(BaseModel):
    """ Representation of an owner"""

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
