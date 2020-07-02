#!/usr/bin/python3
'Base Model creation'

from datetime import datetime
import uuid
import models


class BaseModel:
    'Base class created. It inherates the base data'

    def __init__(self, *args, **kwargs):
        'Constructor for the BaseModel Cls\
        COntains the basics to the future classes'

        if (kwargs):
            for keys, values in self.__dict__.items():
                if keys != '__class__':
                    if keys == "created_at" or keys == "updated_at":
                        valt = datetime.strptime(values,
                                                 "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, keys, valt)
                    else:
                        setattr(self, keys, values)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        'String representation for instances'
        return("[{}] ({}) <{}>".format
               (type(self).__name__, self.id, self.__dict__))

    def save(self):
        'Saves date and time for each update'
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        'Converts the object on a dictionary'
        ob_to_dict = self.__dict__.copy()
        ob_to_dict['created_at'] = self.created_at.isoformat()
        ob_to_dict['updated_at'] = self.updated_at.isoformat()
        ob_to_dict['__class__'] = self.__class__.__name__
        return ob_to_dict
