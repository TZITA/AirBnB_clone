#!/usr/bin/python3
""" Unit tests for the base model. """
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """ A class of all the unittests for the base model."""
    def test_id(self):
        """ Asserts that the type of the attribute id is str."""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Asserts the type of attribute created_at is datetime.datetime."""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Asserts the type of attribute updated_at is datetime.datetime."""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)

    def test_save(self):
        """ Asserts that the attribute updated_at in:
                - the new instance, and
                - the updated form of that instance
            are of diffrent values.
        """
        new = BaseModel()
        u1 = new.updated_at
        new.save()
        u2 = new.updated_at
        self.assertEqual(u1, u2)
