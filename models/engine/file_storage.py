#!/usr/bin/python3
"""Contains FileStorage class"""
import json
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
        """deserializes the JSON file to __objects(only if __file_path exists)"""
        try:
            with open(self.__file_path, 'r') as f:
                json_obj_unloaded = json.load(f)
            for key, json_obj_unloaded in json_obj_unloaded:
                class_name, json_obj_unloaded = key.split(".")
                json_obj_unloaded["created_at"] = datetime.fromisoformat()
                json_obj_unloaded["updated_at"] = datetime.fromisoformat()
                clss = globals()[class_name]
                obj = clss(**json_obj_unloaded)
                self.__objects[key] = obj
        except:
            pass
