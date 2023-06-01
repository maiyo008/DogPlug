#!/usr/bin/python3
""" Unittests for Town module"""
import unittest
from models.town import Town


class TestTown(unittest.TestCase):
    def setUp(self):
        self.town = Town()

    def tearDown(self):
        self.town = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.town, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.town, "name"))
        self.assertTrue(hasattr(self.town, "county_id"))

    def test_attribute_types(self):
        self.assertIsInstance(self.town.name, str)
        self.assertIsInstance(self.town.county_id, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.town.name, "")
        self.assertEqual(self.town.county_id, "")

    def test_initialization_with_kwargs(self):
        town_data = {
            "name": "Springfield",
            "county_id": "12345"
        }
        town = Town(**town_data)

        self.assertEqual(town.name, "Springfield")
        self.assertEqual(town.county_id, "12345")

    def test_to_dict_method(self):
        self.town.name = "Springfield"
        self.town.county_id = "12345"

        town_dict = self.town.to_dict()

        self.assertIsInstance(town_dict, dict)
        self.assertEqual(town_dict["name"], "Springfield")
        self.assertEqual(town_dict["county_id"], "12345")


if __name__ == '__main__':
    unittest.main()
