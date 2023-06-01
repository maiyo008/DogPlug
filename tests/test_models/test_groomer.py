#!/usr/bin/python3
"""Unittests for Groomer Module"""
import unittest
from models.groomer import Groomer


class TestGroomer(unittest.TestCase):
    def setUp(self):
        self.groomer = Groomer()

    def tearDown(self):
        self.groomer = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.groomer, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.groomer, "name"))
        self.assertTrue(hasattr(self.groomer, "email"))
        self.assertTrue(hasattr(self.groomer, "contact"))
        self.assertTrue(hasattr(self.groomer, "service_id"))
        self.assertTrue(hasattr(self.groomer, "review_id"))
        self.assertTrue(hasattr(self.groomer, "location_id"))

    def test_attribute_types(self):
        self.assertIsInstance(self.groomer.name, str)
        self.assertIsInstance(self.groomer.email, str)
        self.assertIsInstance(self.groomer.contact, str)
        self.assertIsInstance(self.groomer.service_id, str)
        self.assertIsInstance(self.groomer.review_id, str)
        self.assertIsInstance(self.groomer.location_id, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.groomer.name, "")
        self.assertEqual(self.groomer.email, "")
        self.assertEqual(self.groomer.contact, "")
        self.assertEqual(self.groomer.service_id, "")
        self.assertEqual(self.groomer.review_id, "")
        self.assertEqual(self.groomer.location_id, "")

    def test_initialization_with_kwargs(self):
        groomer_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "contact": "123-456-7890",
            "service_id": "service_123",
            "review_id": "review_456",
            "location_id": "location_789"
        }
        groomer = Groomer(**groomer_data)

        self.assertEqual(groomer.name, "John Doe")
        self.assertEqual(groomer.email, "john@example.com")
        self.assertEqual(groomer.contact, "123-456-7890")
        self.assertEqual(groomer.service_id, "service_123")
        self.assertEqual(groomer.review_id, "review_456")
        self.assertEqual(groomer.location_id, "location_789")

    def test_to_dict_method(self):
        self.groomer.name = "Jane Smith"
        self.groomer.email = "jane@example.com"
        self.groomer.contact = "987-654-3210"
        self.groomer.service_id = "service_789"
        self.groomer.review_id = "review_123"
        self.groomer.location_id = "location_456"

        groomer_dict = self.groomer.to_dict()

        self.assertIsInstance(groomer_dict, dict)
        self.assertEqual(groomer_dict["name"], "Jane Smith")
        self.assertEqual(groomer_dict["email"], "jane@example.com")
        self.assertEqual(groomer_dict["contact"], "987-654-3210")
        self.assertEqual(groomer_dict["service_id"], "service_789")
        self.assertEqual(groomer_dict["review_id"], "review_123")
        self.assertEqual(groomer_dict["location_id"], "location_456")


if __name__ == '__main__':
    unittest.main()
