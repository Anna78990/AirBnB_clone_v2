#!/usr/bin/python3
""" practice of flask """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ print hello world """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print HBNB """
    return "HBNB"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
