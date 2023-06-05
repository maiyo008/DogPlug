#!/usr/bin/python3
""" Handles RESTful API actions for dogs """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.dog import Dog


@app_views.route('/dogs', methods=['GET'], strict_slashes=False)
def get_dogs():
    """ Retrieve all dogs objects """
    all_dogs = storage.all(Dog).values()
    list_dogs = []
    for dog in all_dogs:
        list_dogs.append(dog.to_dict())
    return jsonify(list_dogs)


@app_views.route('/dogs/<dog_id>', methods=['GET'], strict_slashes=False)
def get_dog(dog_id):
    """ Retrieve a specific dog object"""
    dog = storage.get(Dog, dog_id)
    if not dog:
        abort(404)
    return jsonify(dog.to_dict())


@app_views.route('/dogs/<dog_id>', methods=['DELETE'], strict_slashes=False)
def delete_dog(dog_id):
    """ Delete a specific dog object"""
    dog = storage.get(Dog, dog_id)
    if not dog:
        abort(404)
    storage.delete(dog)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/dogs', methods=['POST'], strict_slashes=False)
def post_dog():
    """ Create a dog object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'breed' not in request.get_json():
        abort(400, description="Missing breed")
    if 'weight' not in request.get_json():
        abort(400, description="Weight missing")
    if 'age' not in request.get_json():
        abort(400, description="Missing age")
    if 'owner_id' not in request.get_json():
        abort(400, description="Missing owner id")

    
    data = request.get_json()
    instance = Dog(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/dogs/<dog_id>', methods=['PUT'], strict_slashes=False)
def put_dog(dog_id):
    """ Updates a specific Dog object"""
    dog = storage.get(Dog, dog_id)
    if not dog:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(dog, key, value)
    storage.save()
    return make_response(jsonify(dog.to_dict()), 200)
