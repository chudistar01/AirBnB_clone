#!/usr/bin/python3
"""
Responsible for serilization and deserilization
of JSON type
"""


import json
from models.base_model import BaseModel

class FileStorage:
    """
    class for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return __objects(a dictionary)
        """
        return self.__objects

    def new(self, object):
        """
        sets in __objects the obj with key 
        <obj class name>.id
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes __objects
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                        }, f)

    def reload(self):
        """
        Deseriliazation
        """
        try:
            with open(__file_path, 'r') as f:
                data = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
