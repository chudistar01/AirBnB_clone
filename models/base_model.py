#!/usr/bin/python3
"""
Base class for AirBnB Project
"""

import uuid
import datetime
import models

class BaseModel:
    """
    Base class

    Attributes:
    id: unique user identity when an instance is created
    created_at: current datetime when an instance is created
    updated_at: updates current time

    Methods:
    __str__: prints class name, id, and dictionary representation of
    instance created
    save(self): updates the public instance
    attribute updated_at with the current datetime
    to_dict(self): returns a dictionary containing all
    keys/values of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        public instance attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        returns string representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at: datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary representation of instance attributes
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
