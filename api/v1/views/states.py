#!/usr/bin/python3
<<<<<<< HEAD
"""
Creates a new view for the states route
and handles RESTful API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State


# This route handles GET and POST requests for States
@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def states():
    """ Handles GET and POST methods for /states"""

    if request.method == 'GET':
        new_list = []  # This list will store all retrieved objects
        objs = storage.all(State)

        for _, value in objs.items():
            new_list.append(value.to_dict())

        return make_response(jsonify(new_list), 200)

    elif request.method == 'POST':
        data = request.get_json()  # This retrieves all the URL parameters
        if data is None:
            abort(400, 'Not a JSON')

        if 'name' not in data:
            abort(400, 'Missing name')

        new_state = State(**data)
        storage.new(new_state)
        storage.save()
        return make_response(jsonify(new_state.to_dict()), 201)
    else:
        abort(405)


@app_views.route(
        '/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
        strict_slashes=False)
def states_id(state_id):
    """
    Handles GET, DELETE, PUT methods for /states/<state_id>
    """
    if request.method == 'GET':
        new_list = []

        obj = storage.get(State, state_id)
        if obj is None:
            abort(404)

        new_list.append(obj.to_dict())
        return make_response(jsonify(new_list), 200)

    elif request.method == 'DELETE':
        obj = storage.get(State, state_id)
        if obj is None:
            abort(404)

        obj.delete()
        storage.save()
        return make_response(jsonify({}), 200)

    elif request.method == 'PUT':
        request_state = request.get_json()
        if request_state is None:
            abort(400, 'Not a JSON')
        state = storage.get(State, state_id)
        if state is None:
            abort(404)

        for i, j in request_state.items():
            if i not in ["id", "state_id", "created_at", "updated_at"]:
                setattr(state, i, j)
        storage.save()
        return make_response(jsonify(state.to_dict()), 200)
    else:
        abort(405)
=======
""" view for State objects"""

from flask import Flask
from flask import Flask, abort
from api.v1.views import app_views
from os import name
from models.state import State
from flask import request


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def toGet():
    '''getting thing'''
    objects = storage.all('State')
    lista = []
    for state in objects.values():
        lista.append(state.to_dict())
    return jsonify(lista)


@app_views.route('/states/<string:stateid>', methods=['GET'],
                 strict_slashes=False)
def toGetid():
    '''Updates a State object id'''
    objects = storage.get('State', 'state_id')
    if objects is None:
        abort(404)
    return jsonify(objects.to_dict()), 'OK'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def posting():
    '''Creates a State'''
    response = request.get_json()
    if response id None:
        abort(400, {'Not a JSON'})
    if "name" not in response:
        abort(400, {'Missing name'})
    stateObject = State(name=response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def putinV():
   """ vladimir"""
    response = request.get_json()
    if response id None:
        abort(400, {'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting():
    ''' to delete an onbject'''
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), '200'
>>>>>>> refs/remotes/origin/main
