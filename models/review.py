#!/usr/bin/python3
""" Review module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """ A representation of a review"""
    if storage_type == "db":
        __tablename__ = "reviews"
        description = Column(String(256), nullable=True)
        star_rating = Column(Integer, nullable=True)
        owner_id = Column(String(40), ForeignKey("owners.id"), nullable=False)
        groomer_id = Column(String(40), ForeignKey("groomers.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialization of a review object"""
        if kwargs:
            super().__init__(*args, **kwargs)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            super().__init__()
            self.description = ""
            self.star_rating = 0
