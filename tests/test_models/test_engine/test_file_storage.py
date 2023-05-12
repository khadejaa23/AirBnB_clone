#!/usr/bin/python3
"""Unittest for FileStorage class"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Sets up test environment"""
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the all() method"""
        f = FileStorage()
        self.assertEqual(f.all(), {})

    def test_save_reload(self):
        """Test the save() and reload() methods"""
        a = BaseModel()
        fs1 = FileStorage()
        fs1.new(a)
        fs1.save()
        fs2 = FileStorage()
        fs2.reload()
        key = a.__class__.__name__ + "." + a.id
        self.assertTrue(fs2.all().get(key))

if __name__ == "__main__":
    unittest.main()
