#!/usr/bin/python3
""" The basic model that defines all common attributes/methods
    for other classes.
"""
import uuid
import datetime
import models


class BaseModel():
    """ A base model that defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Instantiation of the class base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif (k == 'created_at' or k == 'updated_at'):
                    format = '%Y-%m-%dT%H:%M:%S.%f'
                    v = datetime.datetime.strptime(v, format)
                setattr(self, k, v)
        models.storage.new(self)

    def __setitem__(self, key, value):
        """ Enables this class to support item assignment"""
        setattr(self, key, value)
        models.storage.save()

    def save(self):
        """ Update instance attr. updated_at with current datetime."""
        models.storage.save()

    def to_dict(self):
        """ Returns a dict containing all keys/values in __dict__ of insta"""
        todict = {}
        for k, v in self.__dict__.items():
            if (k == 'created_at' or k == 'updated_at'):
                v = v.isoformat()
            todict[k] = v
        todict['__class__'] = self.__class__.__name__
        return todict

    def __str__(self):
        """ String representation of the base model class."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)
