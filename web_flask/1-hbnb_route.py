#!/usr/bin/python3
"""starts a Flask web application."""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """returns a string at the root route"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
