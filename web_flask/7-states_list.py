#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Fetch list o states from storage and place in rendered template """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """ close SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run()
