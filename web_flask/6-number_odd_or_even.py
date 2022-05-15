#!/usr/bin/python3
""" practice of flask """
from flask import Flask, render_template
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


@app.route('/number/<int:path>', strict_slashes=False)
def show_your_text_number(path):
    """ print 'path' is a number """
    return '{} is a number'.format(path)


@app.route('/number_template/<int:path>', strict_slashes=False)
def show_your_number_template(path):
    """ print the path after /number_template/ if it is number """
    return render_template('5-number.html', number=path)


@app.route('/number_odd_or_even/<int:path>', strict_slashes=False)
def show_your_number_odd_even(path):
    """ print the path after /number_odd_or_even/ if it is number """
    html = '6-number_odd_or_even.html'
    if int(path) % 2 == 1:
        return render_template(html, number=path, oe="odd")
    else:
        return render_template(html, number=path, oe="even")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
