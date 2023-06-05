#!/usr/bin/python3
""" Handles RESTful API actions for owners """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.owner import Owner


@app_views.route('/owners', methods=['GET'], strict_slashes=False)
def get_owners():
    """ Retrieve list of all Owner objects"""
    all_owners = storage.all(Owner).values()
    list_owners = []
    for owner in all_owners:
        list_owners.append(owner.to_dict())
    return jsonify(list_owners)


@app_views.route('/owners/<owner_id>', methods=['GET'], strict_slashes=False)
def get_owner(owner_id):
    """ Retrieves a specific Owner object"""
    owner = storage.get(Owner, owner_id)
    if not owner:
        abort(404)
    return jsonify(owner.to_dict())


@app_views.route('/owners/<owner_id>', methods=['DELETE'], strict_slashes=False)
def delete_owner(owner_id):
    """ Delete a specific owner object"""
    owner = storage.get(Owner, owner_id)
    if not owner:
        abort(404)
    storage.delete(owner)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/owners', methods=['POST'], strict_slashes=False)
def post_owner():
    """ Create a owner object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'contact' not in request.get_json():
        abort(400, description="Missing contact")
    
    data = request.get_json()
    instance = Owner(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/owners/<owner_id>', methods=['PUT'], strict_slashes=False)
def put_owner(owner_id):
    """ Updates a specific Owner object"""
    owner = storage.get(Owner, owner_id)
    if not owner:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at', 'review_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(owner, key, value)
    storage.save()
    return make_response(jsonify(owner.to_dict()), 200)
