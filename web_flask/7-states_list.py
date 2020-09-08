#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(close_storage):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_html():
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
