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


    def all(self):
        """ Returns objects """
        return FileStorage.__objects
    

    def new(self, obj):
        """ Assign an obj to __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()
    

    def save(self):
        """ Serialize __objects to a json file """
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(FileStorage.__objects, f)
        except Exception as e:
            print("An error occured: ", e)
    

    def reload(self):
        """ Deserialize __objects from json file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception as e:
            pass