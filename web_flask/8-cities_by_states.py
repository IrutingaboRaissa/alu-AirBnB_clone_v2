#!/usr/bin/python3
"""
Flask web application that displays cities by states.

Routes:
    /cities_by_states: Displays a list of states and associated cities.
    
Teardown:
    Closes the storage session after each request.
"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)  


@app.teardown_appcontext
def teardown(exception):
    """
    Method to handle app context teardown.
    
    This method is called after each request to clean up the session.
    It ensures that the connection to the storage system is properly closed.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    Route handler for displaying a list of states and their cities.
    
    Fetches all State objects from storage and passes them to the template 
    for rendering the list of states and their associated cities.
    
    Returns:
        Rendered HTML page displaying states and cities.
    """
    states = storage.all(State)  # Retrieve all State objects from storage
    return render_template('8-cities_by_states.html', states=states)  # Pass states to the template


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
