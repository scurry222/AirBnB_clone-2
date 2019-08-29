#!/usr/bin/python3
"""  """
from flask import flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_flask():
    """ returns intro string """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
