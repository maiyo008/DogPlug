#!/usr/bin/python3
""" Unittests for Owner module"""
import unittest
from models.owner import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner()

    def tearDown(self):
        self.owner = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.owner, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.owner, "name"))
        self.assertTrue(hasattr(self.owner, "email"))
        self.assertTrue(hasattr(self.owner, "contact"))
        self.assertTrue(hasattr(self.owner, "dog_id"))
        self.assertTrue(hasattr(self.owner, "location_id"))

    def test_attribute_types(self):
        self.assertIsInstance(self.owner.name, str)
        self.assertIsInstance(self.owner.email, str)
        self.assertIsInstance(self.owner.contact, str)
        self.assertIsInstance(self.owner.dog_id, str)
        self.assertIsInstance(self.owner.location_id, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.owner.name, "")
        self.assertEqual(self.owner.email, "")
        self.assertEqual(self.owner.contact, "")
        self.assertEqual(self.owner.dog_id, "")
        self.assertEqual(self.owner.location_id, "")

    def test_initialization_with_kwargs(self):
        owner_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "contact": "1234567890",
            "dog_id": "dog_123",
            "location_id": "location_456"
        }
        owner = Owner(**owner_data)

        self.assertEqual(owner.name, "John Doe")
        self.assertEqual(owner.email, "john@example.com")
        self.assertEqual(owner.contact, "1234567890")
        self.assertEqual(owner.dog_id, "dog_123")
        self.assertEqual(owner.location_id, "location_456")

    def test_to_dict_method(self):
        self.owner.name = "John Doe"
        self.owner.email = "john@example.com"
        self.owner.contact = "1234567890"
        self.owner.dog_id = "dog_123"
        self.owner.location_id = "location_456"

        owner_dict = self.owner.to_dict()

        self.assertIsInstance(owner_dict, dict)
        self.assertEqual(owner_dict["name"], "John Doe")
        self.assertEqual(owner_dict["email"], "john@example.com")
        self.assertEqual(owner_dict["contact"], "1234567890")
        self.assertEqual(owner_dict["dog_id"], "dog_123")
        self.assertEqual(owner_dict["location_id"], "location_456")

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
