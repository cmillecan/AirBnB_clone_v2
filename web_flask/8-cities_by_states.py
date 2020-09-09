#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(close):
    """Closes session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_state_html():
    """Displays HTML page"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
