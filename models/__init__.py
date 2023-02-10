#!/usr/bin/python3
""" Creates a FileStorage instance of the App."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
