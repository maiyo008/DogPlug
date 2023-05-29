#!/usr/bin/python3
""" Unittests for Service module"""
import unittest
from models.service import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    def tearDown(self):
        self.service = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.service, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.service, "description"))
        self.assertTrue(hasattr(self.service, "duration"))
        self.assertTrue(hasattr(self.service, "price"))

    def test_attribute_types(self):
        self.assertIsInstance(self.service.description, str)
        self.assertIsInstance(self.service.duration, str)
        self.assertIsInstance(self.service.price, int)

    def test_attribute_defaults(self):
        self.assertEqual(self.service.description, "")
        self.assertEqual(self.service.duration, "")
        self.assertEqual(self.service.price, 0)

    def test_initialization_with_kwargs(self):
        service_data = {
            "description": "Grooming Service",
            "duration": "1 hour",
            "price": 50
        }
        service = Service(**service_data)

        self.assertEqual(service.description, "Grooming Service")
        self.assertEqual(service.duration, "1 hour")
        self.assertEqual(service.price, 50)

    def test_to_dict_method(self):
        self.service.description = "Grooming Service"
        self.service.duration = "1 hour"
        self.service.price = 50

        service_dict = self.service.to_dict()

        self.assertIsInstance(service_dict, dict)
        self.assertEqual(service_dict["description"], "Grooming Service")
        self.assertEqual(service_dict["duration"], "1 hour")
        self.assertEqual(service_dict["price"], 50)


if __name__ == '__main__':
    unittest.main()
