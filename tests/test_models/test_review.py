#!/usr/bin/python3
""" Unittests for Review module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        self.review = None

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "description"))
        self.assertTrue(hasattr(self.review, "star_rating"))

    def test_attribute_types(self):
        self.assertIsInstance(self.review.description, str)
        self.assertIsInstance(self.review.star_rating, int)

    def test_attribute_defaults(self):
        self.assertEqual(self.review.description, "")
        self.assertEqual(self.review.star_rating, 0)

    def test_initialization_with_kwargs(self):
        review_data = {
            "description": "Great service!",
            "star_rating": 5
        }
        review = Review(**review_data)

        self.assertEqual(review.description, "Great service!")
        self.assertEqual(review.star_rating, 5)

    def test_to_dict_method(self):
        self.review.description = "Great service!"
        self.review.star_rating = 5

        review_dict = self.review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["description"], "Great service!")
        self.assertEqual(review_dict["star_rating"], 5)


if __name__ == '__main__':
    unittest.main()
