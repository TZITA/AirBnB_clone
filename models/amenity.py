#!/usr/bin/python3
"""Defines an amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class amenity inherts from BaseModel class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation of amenity class."""
        super().__init__(*args, **kwargs)
