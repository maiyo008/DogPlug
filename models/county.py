#!/usr/bin/python3
""" County module """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class County(BaseModel, Base):
    """ A representation of a county """
    if models.storage_type == "db":
        __tablename__ = "counties"
        name = Column(String(100), nullable=False)
        towns = relationship(
            "Town",
            backref="county",
            cascade="all, delete, delete-orphan"
        )

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
    
    if models.storage_type != "db":
        @property
        def towns(self):
            """ Getter for list of town instances related to counties """
            town_list = []
            all_towns = models.storage.all(town)
            for town in all_towns.value():
                if town.county_id == self.id:
                    town_list.append(town)
            return town_list