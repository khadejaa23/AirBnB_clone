#!/usr/bin/python3
"""this module defines all common attributes/methods for other classes"""
import  uuid
import models
from datetime import datetime

class BaseModel:
    """This class defines a base mode"""
    def __init__(self, *args, **kwargs):
        """initialization method
        Arguments:
            *args: Non-keyworded variable argument list (not used here)
            **kwargs: Handles named arguments passed
        """
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """this method prints id, created_at, updated_at public attributes"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates th updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the insnstance"""
        dict_object = self.__dict__.copy()
        dict_object["__class__"] = self.__class__.__name__
        dict_object["created_at"] = self.created_at.isoformat()
        dict_object["updated_at"] = self.updated_at.isoformat()
        return dict_object
