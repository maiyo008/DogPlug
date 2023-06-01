#!/usr/bin/python3
""" Unittests for location modules"""
import unittest
from models.location import Location


class TestLocation(unittest.TestCase):
    def setUp(self):
        self.location = Location()

    def tearDown(self):
        self.location = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.location, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.location, "longitude"))
        self.assertTrue(hasattr(self.location, "latitude"))
        self.assertTrue(hasattr(self.location, "town_id"))
        self.assertTrue(hasattr(self.location, "county_id"))

    def test_attribute_types(self):
        self.assertIsInstance(self.location.longitude, str)
        self.assertIsInstance(self.location.latitude, str)
        self.assertIsInstance(self.location.town_id, str)
        self.assertIsInstance(self.location.county_id, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.location.longitude, "")
        self.assertEqual(self.location.latitude, "")
        self.assertEqual(self.location.town_id, "")
        self.assertEqual(self.location.county_id, "")

    def test_initialization_with_kwargs(self):
        location_data = {
            "longitude": "12.3456",
            "latitude": "-98.7654",
            "town_id": "town_123",
            "county_id": "county_456"
        }
        location = Location(**location_data)

        self.assertEqual(location.longitude, "12.3456")
        self.assertEqual(location.latitude, "-98.7654")
        self.assertEqual(location.town_id, "town_123")
        self.assertEqual(location.county_id, "county_456")

    def test_to_dict_method(self):
        self.location.longitude = "12.3456"
        self.location.latitude = "-98.7654"
        self.location.town_id = "town_123"
        self.location.county_id = "county_456"

        location_dict = self.location.to_dict()

        self.assertIsInstance(location_dict, dict)
        self.assertEqual(location_dict["longitude"], "12.3456")
        self.assertEqual(location_dict["latitude"], "-98.7654")
        self.assertEqual(location_dict["town_id"], "town_123")
        self.assertEqual(location_dict["county_id"], "county_456")


if __name__ == '__main__':
    unittest.main()
