#!/usr/bin/python3
"""this module tests the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    def test_init(self):
        """Tests the initialization"""
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)
        self.assertIsNotNone(a.created_at)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsNotNone(a.updated_at)
        self.assertIsInstance(a.updated_at, datetime)
        self.assertIsNotNone(a.id)

    def test_uniqueId(self):
        """Tests the uniqueness of generated ID"""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_dict(self):
        """Tests the to_dict() method"""
        a = BaseModel()
        dic = a.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic["id"], a.id)

if __name__ == '__main__':
    unittest.main()
