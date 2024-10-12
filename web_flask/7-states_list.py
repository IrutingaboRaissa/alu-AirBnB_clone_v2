#!/usr/bin/python3
"""Module that starts a Flask web application."""

import os
import sys
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Return an HTML page with a list of all States in the database."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Close the session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
