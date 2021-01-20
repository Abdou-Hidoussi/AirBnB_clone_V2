#!/usr/bin/python3
""" Task 0 """
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def exeption(e):
    """ Task 8 """
    storage.close()


@app.route('/states_list')
def statesList():
    """ Task 8 """
    state = storage.all("State")
    return render_template('7-states_list.html', state=state)


if __name__ == "__main__":
    app.run()
