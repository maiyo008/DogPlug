#!/usr/bin/python3
""" Handles RESTful API actions for towns """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.town import Town


@app_views.route('/towns', methods=['GET'], strict_slashes=False)
def get_towns():
    """ Retrieve list of all Town objects"""
    all_towns = storage.all(Town).values()
    list_towns = []
    for town in all_towns:
        list_towns.append(town.to_dict())
    return jsonify(list_towns)


@app_views.route('/towns/<town_id>', methods=['GET'], strict_slashes=False)
def get_town(town_id):
    """ Retrieves a specific Town object"""
    town = storage.get(Town, town_id)
    if not town:
        abort(404)
    return jsonify(town.to_dict())


@app_views.route('/towns/<town_id>', methods=['DELETE'], strict_slashes=False)
def delete_town(town_id):
    """ Delete a specific town object"""
    town = storage.get(Town, town_id)
    if not town:
        abort(404)
    storage.delete(town)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/towns', methods=['POST'], strict_slashes=False)
def post_town():
    """ Create a town object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'county_id' not in request.get_json():
        abort(400, description="Missing county_id")
    
    data = request.get_json()
    instance = Town(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/towns/<town_id>', methods=['PUT'], strict_slashes=False)
def put_town(town_id):
    """ Updates a specific Town object"""
    town = storage.get(Town, town_id)
    if not town:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(town, key, value)
    storage.save()
    return make_response(jsonify(town.to_dict()), 200)
