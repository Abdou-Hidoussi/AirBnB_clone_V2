#!/usr/bin/python3
""" Task 0 """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def rootdict():
    """ Task 0 """
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnbdict():
    """ Task 1 """
    return "HBNB"


@app.route("/c/<text>")
def cdict(text):
    """ Task 2 """
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python/<text>")
@app.route("/python/")
def pydict(text="is cool"):
    """ Task 3 """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<n>")
def numberdict(n):
    """ Task 4 """
    try:
        nb = int(n)
        return ("{} is a number".format(nb))
    except Exception:
        abort(404)


@app.route("/number_template/<n>")
def nbtempdict(n):
    """ Task 5 """
    try:
        nb = int(n)
        return render_template('5-number.html', nb=nb)
    except Exception:
        abort(404)

if __name__ == '__main__':
    app.run()
