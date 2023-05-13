#!/usr/bin/python3
"""Contains FileStorage class"""
import json
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    """Class serializes and deserializes JSON files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file '__file_path'"""
        json_obj = {}
        for key, obj in self.__objects.items():
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects(if __file_path exists)"""
        try:
            with open(self.__file_path, 'r') as f:
                FileStorage.__objects = {}
                json_obj_unloaded = json.load(f)
                for key in json_obj_unloaded.keys():
                    clss = json_obj_unloaded[key].pop("__class__", None)
                    created_at = json_obj_unloaded[key]["created_at"]
                    created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
                    updated_at = json_obj_unloaded[key]["updated_at"]
                    updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")
                    FileStorage.__objects[key] = eval(clss)(json_obj_unloaded[key])
        except FileNotFoundError:
            pass
