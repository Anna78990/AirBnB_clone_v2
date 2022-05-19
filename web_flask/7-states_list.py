#!/usr/bin/python3
""" practice of flask """
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception):
    """Close session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_state():
    """ print state list """
    states = storage.all(State).values()
    return render_template("7-states_list.html", state=states)

if __name__ == '__main__':
    app.run(host="0.0.0.0" port=5000)
