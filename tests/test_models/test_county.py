#!/usr/bin/python3
"""Test county module"""
import unittest
from models.county import County


class TestCounty(unittest.TestCase):
    def setUp(self):
        self.county = County()

    def tearDown(self):
        self.county = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.county, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.county, "name"))

    def test_attribute_types(self):
        self.assertIsInstance(self.county.name, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.county.name, "")

    def test_to_dict_method(self):
        self.county.name = "Test County"

        county_dict = self.county.to_dict()

        self.assertIsInstance(county_dict, dict)
        self.assertEqual(county_dict["name"], "Test County")

if __name__ == '__main__':
    unittest.main()
