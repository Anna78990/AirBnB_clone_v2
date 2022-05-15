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


@app.route('/', defaults={'path': ''})
@app.route('/c/<path:path>', strict_slashes=False)
def show_your_text(path):
    """ print C is 'path' """
    path = path.replace('_', ' ')
    return 'C %s' % path


@app.route('/python', strict_slashes=False)
@app.route('/python/<path>', strict_slashes=False)
def show_your_text_python(path="is_cool"):
    """ print Python is 'path' """
    path = path.replace('_', ' ')
    return 'Python %s' % path


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
