#!/usr/bin/python3
""" service module """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, ForeignKey


class Service(BaseModel, Base):
    """ A representation of service"""
    if storage_type == "db":
        __tablename__ = "services"
        description = Column(String(256), nullable=False, default="")
        duration = Column(String(20), nullable=False, default="")
        price = Column(Integer, nullable=False, default=0)
        groomer_id = Column(String(40), ForeignKey("groomers.id"), nullable=False)

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
