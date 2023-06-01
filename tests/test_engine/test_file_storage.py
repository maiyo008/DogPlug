#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.county import County


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        self.file_storage = None

    def test_initialization(self):
        self.assertEqual(self.file_storage._FileStorage__file_path, "file.json")
        #self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_all_method(self):
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, self.file_storage._FileStorage__objects)

    def test_all_method_with_cls(self):
        base_model = BaseModel()
        county = County()
        self.file_storage.new(base_model)
        self.file_storage.new(county)

        base_model_objects = self.file_storage.all(BaseModel)
        county_objects = self.file_storage.all(County)

        self.assertIn(f"{base_model.__class__.__name__}.{base_model.id}", base_model_objects)
        self.assertNotIn(f"{county.__class__.__name__}.{county.id}", base_model_objects)

        self.assertIn(f"{county.__class__.__name__}.{county.id}", county_objects)
        self.assertNotIn(f"{base_model.__class__.__name__}.{base_model.id}", county_objects)

    def test_new_method(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, self.file_storage._FileStorage__objects)
        self.assertEqual(self.file_storage._FileStorage__objects[key], base_model)

    def test_save_method(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()

        # TODO: Validate that the file was saved correctly

    def test_reload_method(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()

        reloaded_file_storage = FileStorage()
        reloaded_file_storage.reload()

        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, reloaded_file_storage._FileStorage__objects)
        self.assertIsInstance(reloaded_file_storage._FileStorage__objects[key], BaseModel)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
