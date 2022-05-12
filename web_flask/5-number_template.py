from flask import Flask, abort, render_template
""" practice of flask """


app = Flask(__name__)


""" print hello world """
@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


""" print hello HBNB """
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


""" print the path after /c/ """
@app.route('/', defaults={'path': ''})
@app.route('/c/<path:path>', strict_slashes=False)
def show_your_text(path):
    path = path.replace('_', ' ')
    return 'C %s' % path


""" print the path after /Python/, if it is empty, print 'is cool'"""
@app.route('/python', strict_slashes=False)
@app.route('/python/<path>', strict_slashes=False)
def show_your_text_python(path="is_cool"):
    path = path.replace('_', ' ')
    return 'Python %s' % path


""" print the path after /number/ if it is number """
@app.route('/number', strict_slashes=False)
@app.route('/number/<path>', strict_slashes=False)
def show_your_text_number(path):
    if path.isdigit():
        return '{} is a number'.format(path)
    else:
        abort(404)


""" print the path after /number_template/ if it is number """
@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<path>', strict_slashes=False)
def show_your_number_template(path):
    if path.isdigit():
        return render_template('5-number.html', number=path)
    else:
        abort(404)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
