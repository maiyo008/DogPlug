#!/usr/bin/python3
"""
This module creates a FileStorage class.
The class will be used in serialization to json, 
and deserialization from json
"""
import json
import models
from models.base_model import BaseModel
from models.county import County
from models.dog import Dog
from models.groomer import Groomer
from models.location import Location
from models.owner import Owner
from models.review import Review
from models.service import Service
from models.town import Town
classes = {
    "BaseModel": BaseModel,
    "County": County,
    "Dog": Dog,
    "Groomer": Groomer,
    "Location": Location,
    "Owner": Owner,
    "Review": Review,
    "Service": Service,
    "Town": Town
}


class FileStorage():
    """
    Serializes objects to a json file,
    and deserializes from the json file back to an object.
    """
    __file_path = "file.json"
    __objects = {}


    def all(self, cls=None):
        """ Returns objects """
        if cls is not None:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects
    

    def new(self, obj):
        """ Assign an obj to __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    

    def save(self):
        """ Serialize __objects to a json file """
        json_objects = {}
        for key, value in FileStorage.__objects.items():
            json_objects[key] = FileStorage.__objects[key].to_dict()
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(json_objects, f)
        except Exception as e:
            print("An error occured: ", e)
    

    def reload(self):
        """ Deserialize __objects from json file to __objects"""
        
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_reload = json.load(f)
                for key in json_reload:
                    FileStorage.__objects[key] = classes[json_reload[key]["__class__"]](**json_reload[key])
        except Exception as e:
            pass
    
    def delete(self, obj=None):
        """ Delete an object instance if it exists """
        if obj is not None:
            key = "{}.{}".format(
                obj.__class__.__name__,
                obj.id
            )
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
    
    def close(self):
        """Call reload method to deserialize json to objects"""
        self.reload()
    
    def get(self, cls, id):
        """Returns an object specified by its class and its id"""
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None
    
    def count(self, cls=None):
        """ Counts the objects of a particular class,
        if no class is specified counts all the objects in storage
        """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count += len(models.storage.all(cls).values())
        return count
