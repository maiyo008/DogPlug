#!/usr/bin/python3
""" Dog module """
from models.base_model import BaseModel


class Dog(BaseModel):
    """ A representation of a dog """
    def __init__(self, *args, **kwargs):
        """ Initialize a dog object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.name = ""
            self.breed = ""
            self.weight = 0
            self.age = 0            
