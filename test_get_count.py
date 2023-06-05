#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.county import County

print("All objects: {}".format(storage.count()))
print("County objects: {}".format(storage.count(County)))

first_county_id = list(storage.all(County).values())[0].id
print("First county: {}".format(storage.get(County, first_county_id)))