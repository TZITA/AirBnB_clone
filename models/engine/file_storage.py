#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ """
    __file_path = "myfile.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """
        classname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(classname, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file."""
        FSOBJ = FileStorage.__objects
        odict = {obj: FSOBJ[obj].to_dict() for obj in FSOBJ.keys()}
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(odict, fl)

    def reload(self):
        """ Deserializes JSON file to __objects if JSON file exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for ob in objdict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name)(**ob))
        except FileNotFoundError:
            return
