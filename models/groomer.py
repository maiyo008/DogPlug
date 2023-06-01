#!/usr/bin/python3
""" Groomer module """
from models.base_model import BaseModel


class Groomer(BaseModel):
    """ A representation of a groomer"""

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
