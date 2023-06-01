#!/usr/bin/python3
"""
This module creates a base model for all the other classes for the project.
The class here is going to be inherited by all the other classes.
"""
import uuid
from datetime import datetime
from models import storage


time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """
    This class handles the attributes that is common to all other 
    model classes. In addition it will handle basic methods to 
    help in serialization of model objects
    """
   

    def __init__(self, *args, **kwargs):
        """Initializes every instance of this class
        
        Args:
            id(string): a unique identifier for each object
            created_at(datetime): indicate time when an object is created
            updated_at(datetime): indicates time when an object is modified

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    

    def __str__(self):
        """ Returns a string that prints the format
        [<class name>](<obj id>)<self.__dict__>
        """
        return "[{}]({}){}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    

    def to_dict(self):
        """Returns a dictionary containing all the __dict__
        attributes of the instance
        """
        dict_a = {}
        for key, value in self.__dict__.items():
            setattr(self, key, value)
            dict_a[key] = value
        dict_a["__class__"] = self.__class__.__name__
        if "created_at" in dict_a and isinstance(dict_a["created_at"], datetime):
            dict_a["created_at"] = dict_a["created_at"].strftime(time)
        if "updated_at" in dict_a  and isinstance(dict_a["updated_at"], datetime):
            dict_a["updated_at"] = dict_a["updated_at"].strftime(time)
        return dict_a


    def save(self):
        """
        Updates when an instance is modified
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()