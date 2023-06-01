#!/usr/bin/python3
""" service module """
from models.base_model import BaseModel


class Service(BaseModel):
    """ A representation of service"""

    def __init__(self, *args, **kwargs):
        """ Initialization of a service object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.description = ""
            self.duration = ""
            self.price = 0
