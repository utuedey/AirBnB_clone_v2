#!/usr/bin/python3
"""starts a Flask web application."""

from flask import Flask
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
    """ Return a string c and the argument """
    underscore = "_"
    if underscore in text:
        return "C " + text.replace(underscore, " ")
    else:
        return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    underscore = "_"
    if underscore in text:
        return "Python " + text.replace(underscore, " ")
    else:
        return "Python " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
