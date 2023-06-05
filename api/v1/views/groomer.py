#!/usr/bin/python3
""" Handles RESTful API actions for groomers """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.groomer import Groomer


@app_views.route('/groomers', methods=['GET'], strict_slashes=False)
def get_groomers():
    """ Retrieve list of all Groomer objects"""
    all_groomers = storage.all(Groomer).values()
    list_groomers = []
    for groomer in all_groomers:
        list_groomers.append(groomer.to_dict())
    return jsonify(list_groomers)


@app_views.route('/groomers/<groomer_id>', methods=['GET'], strict_slashes=False)
def get_groomer(groomer_id):
    """ Retrieves a specific Groomer object"""
    groomer = storage.get(Groomer, groomer_id)
    if not groomer:
        abort(404)
    return jsonify(groomer.to_dict())


@app_views.route('/groomers/<groomer_id>', methods=['DELETE'], strict_slashes=False)
def delete_groomer(groomer_id):
    """ Delete a specific groomer object"""
    groomer = storage.get(Groomer, groomer_id)
    if not groomer:
        abort(404)
    storage.delete(groomer)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/groomers', methods=['POST'], strict_slashes=False)
def post_groomer():
    """ Create a groomer object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'contact' not in request.get_json():
        abort(400, description="Missing contact")
    
    data = request.get_json()
    instance = Groomer(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/groomers/<groomer_id>', methods=['PUT'], strict_slashes=False)
def put_groomer(groomer_id):
    """ Updates a specific Groomer object"""
    groomer = storage.get(Groomer, groomer_id)
    if not groomer:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at', 'review_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(groomer, key, value)
    storage.save()
    return make_response(jsonify(groomer.to_dict()), 200)
