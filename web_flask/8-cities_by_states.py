#!/usr/bin/python3
""" Task 0 """
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def exeption(e):
    """ Task 8 """
    storage.close()


@app.route('/cities_by_state', strict_slashes=False)
def statesList():
    """ Task 9 """
    state = storage.all("State")
    return render_template('8-cities_by_states.html', state=state)


if __name__ == "__main__":
    app.run()
