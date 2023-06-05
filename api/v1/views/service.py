#!/usr/bin/python3
""" Handles RESTful API actions for services """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.service import Service


@app_views.route('/services', methods=['GET'], strict_slashes=False)
def get_services():
    """ Retrieve all services objects """
    all_services = storage.all(Service).values()
    list_services = []
    for service in all_services:
        list_services.append(service.to_dict())
    return jsonify(list_services)


@app_views.route('/services/<service_id>', methods=['GET'], strict_slashes=False)
def get_service(service_id):
    """ Retrieve a specific service object"""
    service = storage.get(Service, service_id)
    if not service:
        abort(404)
    return jsonify(service.to_dict())


@app_views.route('/services/<service_id>', methods=['DELETE'], strict_slashes=False)
def delete_service(service_id):
    """ Delete a specific service object"""
    service = storage.get(Service, service_id)
    if not service:
        abort(404)
    storage.delete(service)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/services', methods=['POST'], strict_slashes=False)
def post_service():
    """ Create a service object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'description' not in request.get_json():
        abort(400, description="Missing description")
    if 'duration' not in request.get_json():
        abort(400, description="Missing duration")
    if 'price' not in request.get_json():
        abort(400, description="Weight mprice")
    if 'groomer_id' not in request.get_json():
        abort(400, description="Missing groomers_id")
    
    data = request.get_json()
    instance = Service(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/services/<service_id>', methods=['PUT'], strict_slashes=False)
def put_service(service_id):
    """ Updates a specific Service object"""
    service = storage.get(Service, service_id)
    if not service:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at', 'groomer_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(service, key, value)
    storage.save()
    return make_response(jsonify(service.to_dict()), 200)
