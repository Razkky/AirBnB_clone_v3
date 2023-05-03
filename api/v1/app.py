#!/usr/bin/python3
"""Create a web application using Flask
"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)
app.debug = True


@app.teardown_appcontext
def close(error):
    """Close storage after every session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return json object for 404 not found errorr"""
    return make_response(jsonify({
        "error": "Not found"
    }))


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
