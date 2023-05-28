#!/usr/bin/python3
""" County module """
from models.base_model import BaseModel


class County(BaseModel):
    """ A representation of a county """

    def __init__(self, *args, **kwargs):
        """ Initialization of a county object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.name = ""
