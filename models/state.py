#!/usr/bin/python3
""" Defines a State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation of tha state class."""
        super().__init__(*args, **kwargs)
