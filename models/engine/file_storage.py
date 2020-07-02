#!/usr/bin/python3

import json
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State


class FileStorage:
    'Management of persistance'

    __file_path = 'file.json'

    __objects = {}
    all_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def all(self):
        'Return all values'
        return self.__objects

    def new(self, obj):
        'Sets in dict __objects the obj with key class name.id'
        keys = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[keys] = obj

    def save(self):
        'Serializes __objects to JSON files'
        with open(self.__file_path, mode='w') as file:
            json_dict = {}
            for key, objects in self.__objects.items():
                json_dict.update({key: objects.to_dict()})
            file.write(json.dumps(json_dict))

    def reload(self):
        'Deserializes JSON file to __objects dictionary'
        try:
            with open(self.__file_path, mode='r') as jsonf:
                to_ins = json.load(jsonf)
                for key, value in to_ins.items():
                    keys = "{}.{}".format(value["__class__"], value["id"])
                    values = self.all_classes[value["__class__"]](**value)
                    self.__objects[key] = values
        except FileNotFoundError:
            pass
