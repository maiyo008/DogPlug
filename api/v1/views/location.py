#!/usr/bin/python3
""" Handles RESTful API actions for locations """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.location import Location


@app_views.route('/locations', methods=['GET'], strict_slashes=False)
def get_locations():
    """ Retrieve all locations objects """
    all_locations = storage.all(Location).values()
    list_locations = []
    for location in all_locations:
        list_locations.append(location.to_dict())
    return jsonify(list_locations)


@app_views.route('/locations/<location_id>', methods=['GET'], strict_slashes=False)
def get_location(location_id):
    """ Retrieve a specific location object"""
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    return jsonify(location.to_dict())


@app_views.route('/locations/<location_id>', methods=['DELETE'], strict_slashes=False)
def delete_location(location_id):
    """ Delete a specific location object"""
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    storage.delete(location)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/locations', methods=['POST'], strict_slashes=False)
def post_location():
    """ Create a location object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'town_id' not in request.get_json():
        abort(400, description="Missing town_id")
    if 'groomer_id' not in request.get_json():
        abort(400, description="Missing groomers_id")
    
    data = request.get_json()
    instance = Location(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/locations/<location_id>', methods=['PUT'], strict_slashes=False)
def put_location(location_id):
    """ Updates a specific Location object"""
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at', 'groomer_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(location, key, value)
    storage.save()
    return make_response(jsonify(location.to_dict()), 200)
