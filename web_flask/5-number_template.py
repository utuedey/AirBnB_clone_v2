#!/usr/bin/python3
"""starts a Flask web application."""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """returns a string at the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """ Return a string at the /c/text route"""
    underscore = "_"
    if underscore in text:
        return "C " + text.replace(underscore, " ")
    else:
        return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """Return a string at the /python/text route"""
    underscore = "_"
    if underscore in text:
        return "Python " + text.replace(underscore, " ")
    else:
        return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def dispay_n_is_number(n):
    """Return a string at the /number/n route
    only if n is an integer."""
    if type(n) == int:
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html_page(n):
    """returns a template at the /number_template/<n> route"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
