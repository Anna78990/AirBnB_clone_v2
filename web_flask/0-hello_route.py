#!/usr/bin/python3
from flask import Flask
""" practice of flask """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ print hello world """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
