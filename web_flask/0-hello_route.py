#!/usr/bin/python3
""" practice of flask """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ print hello world """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
