#!/usr/bin/python3
"""Defines city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class city inherts from BaseModel class."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation of city class."""
        super().__init__(*args, **kwargs)
