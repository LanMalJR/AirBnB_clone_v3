#!/usr/bin/python3xx

import model
from model import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def returnsomething():
    """Return something"""
    return jsonify(status='OK')
@app_views.route('/stats', strict_slashes=False)
def stuff():
   """ JSON Responses"""
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
