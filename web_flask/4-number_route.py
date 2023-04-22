#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return hello NMBB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Configure C is Fun"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text='is cool'):
    """Configure Python is Fun"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Check and return if it is an integer"""
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
