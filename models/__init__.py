#!/usr/bin/python3
"""This module creates  FileStorage instance and calls reload()"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
