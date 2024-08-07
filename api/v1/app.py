#!/usr/bin/python3
<<<<<<< HEAD
"""This is the main flask app"""

from flask import Flask, jsonify, make_response, render_template
from models import storage
from api.v1.views import app_views
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(err):
    """Handles 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def close_db(error):
    """Handles app teardown"""
    storage.close()


if __name__ == '__main__':
    """Main function"""
    api_host = environ.get('HBNB_API_HOST')
    api_port = environ.get('HBNB_API_PORT')
    if not api_host:
        api_host = '0.0.0.0'
    if not api_port:
        api_port = 5000
    app.run(host=api_host, port=api_port, threaded=True)
=======

""" flask server"""

from flask import flask
from flask import jsonify
from flask api.v1.views import app_views
from models import storage
from os import getenv

app = flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_appcontext(exception):
    """ api status"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """return render_template"""
    return jsonify('error='Not found'), 404

    if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
>>>>>>> refs/remotes/origin/main
