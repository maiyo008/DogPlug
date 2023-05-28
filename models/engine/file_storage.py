#!/usr/bin/python3
"""
This module creates a FileStorage class.
The class will be used in serialization to json, 
and deserialization from json
"""
import json


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
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_reload = json.load(f)
                for key in json_reload:
                    FileStorage.__objects[key] = classes[json_reload[key]["__class__"]](**json_reload[key])
        except Exception as e:
            pass