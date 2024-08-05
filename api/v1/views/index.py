<<<<<<< HEAD
#!/usr/bin/python3
"""
This view handles the /status and /stats routes
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_stats():
    """ Gets status of the function call """
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Returns the count of eash instance type """
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    classes = {
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }

    stats = {}
    for key, value in classes.items():
        count = storage.count(value)
        stats[key.lower()] = count
    return jsonify(stats)
=======
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
>>>>>>> refs/remotes/origin/main
