#!/usr/bin/python3
""" Task 0 """
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def exeption(e):
    """ Task 8 """
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def SABC(id=None):
    """ Task 10 """
    state = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', state=state, id=id)

if __name__ == "__main__":
    app.run()
