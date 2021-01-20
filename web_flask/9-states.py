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
def StatesAndcitiesByState(id=None):
    """ Task 10 """
    state = storage.all("State")
    if id is None:
        return render_template('9-states.html', state=state)
    else:
        for x in state.values():
            if x.id == id:
                return render_template("9-states.html", state=x)
        return render_template("9-states.html")

if __name__ == "__main__":
    app.run()
