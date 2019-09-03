#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """ returns intro string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_flask_1():
    """ returns intro string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_flask(text):
    """ returns text after replacing undescores with spaces """
    string = "C "
    string += text.replace('_', ' ')
    return string

if __name__ == "__main__":
    app.run()
