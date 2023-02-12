#!/usr/bin/python3
"""Defines review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class review inherts from BaseModel class."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation of review class."""
        super().__init__(*args, **kwargs)
