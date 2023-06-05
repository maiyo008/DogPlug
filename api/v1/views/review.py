#!/usr/bin/python3
""" Handles RESTful API actions for reviews """
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models.review import Review


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """ Retrieve all reviews objects """
    all_reviews = storage.all(Review).values()
    list_reviews = []
    for review in all_reviews:
        list_reviews.append(review.to_dict())
    return jsonify(list_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """ Retrieve a specific review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """ Delete a specific review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def post_review():
    """ Create a review object"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'description' not in request.get_json():
        abort(400, description="Missing description")
    if 'star_rating' not in request.get_json():
        abort(400, description="Missing star_rating")
    if 'owner_id' not in request.get_json():
        abort(400, description="Missing owner_id")
    if 'groomer_id' not in request.get_json():
        abort(400, description="Missing groomer_id")
    
    data = request.get_json()
    instance = Review(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """ Updates a specific Review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at', 'groomer_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)
