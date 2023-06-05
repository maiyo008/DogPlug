#!/usr/bin/python3
""" Flask application"""
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ close storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 error
    Responses:
        404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__  == "__main__":
    host = environ.get('DOGPLUG_API_HOST')
    port = environ.get('DOGPLUG_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
