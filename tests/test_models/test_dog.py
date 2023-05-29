#!/usr/bin/python3
""" Unittests for Dog module"""
import unittest
from models.dog import Dog


class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()

    def tearDown(self):
        self.dog = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.dog, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.dog, "name"))
        self.assertTrue(hasattr(self.dog, "breed"))
        self.assertTrue(hasattr(self.dog, "weight"))
        self.assertTrue(hasattr(self.dog, "age"))

    def test_attribute_types(self):
        self.assertIsInstance(self.dog.name, str)
        self.assertIsInstance(self.dog.breed, str)
        self.assertIsInstance(self.dog.weight, int)
        self.assertIsInstance(self.dog.age, int)

    def test_attribute_defaults(self):
        self.assertEqual(self.dog.name, "")
        self.assertEqual(self.dog.breed, "")
        self.assertEqual(self.dog.weight, 0)
        self.assertEqual(self.dog.age, 0)

    def test_initialization_with_kwargs(self):
        dog_data = {
            "name": "Max",
            "breed": "Labrador",
            "weight": 25,
            "age": 5
        }
        dog = Dog(**dog_data)

        self.assertEqual(dog.name, "Max")
        self.assertEqual(dog.breed, "Labrador")
        self.assertEqual(dog.weight, 25)
        self.assertEqual(dog.age, 5)

    def test_to_dict_method(self):
        self.dog.name = "Buddy"
        self.dog.breed = "Golden Retriever"
        self.dog.weight = 30
        self.dog.age = 3

        dog_dict = self.dog.to_dict()

        self.assertIsInstance(dog_dict, dict)
        self.assertEqual(dog_dict["name"], "Buddy")
        self.assertEqual(dog_dict["breed"], "Golden Retriever")
        self.assertEqual(dog_dict["weight"], 30)
        self.assertEqual(dog_dict["age"], 3)


if __name__ == '__main__':
    unittest.main()
