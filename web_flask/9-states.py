#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Fetch cities in passed in state id if provided, all if not """
    if not id:
        states = storage.all('State').values()
    else:
        k = '{}.{}'.format('State', id)
        if k in states:
            states = states[k]
        else:
            states = None

    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """ close SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
