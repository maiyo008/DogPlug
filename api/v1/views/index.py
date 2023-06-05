#!/usr/bin/python3
""" Index file"""
from models.county import County
from models.dog import Dog
from models.groomer import Groomer
from models.location import Location
from models.owner import Owner
from models.review import Review
from models.service import Service
from models.town import Town
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the api"""
    return jsonify({"Status": "ok"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieve the number of each objects by type"""
    classes = [County, Dog, Groomer, Location, Owner, Review, Service, Town]
    names = ["counties", "dogs", "groomers", "locations", "owners", "reviews", "serices", "towns"]
    
    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])
    return jsonify(num_objs)
