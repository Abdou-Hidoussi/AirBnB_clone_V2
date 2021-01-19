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


@app.route("/number/<int:n>")
def numberdict(n):
    """ Task 4 """
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def nbtempdict(n):
    """ Task 5 """
    if isinstance(n, int):
        return render_template('5-number.html', nb=n)


@app.route("/number_odd_or_even/<int:n>")
def evoddict(n):
    """ Task 6 """
    if isinstance(n, int):
        if (n / 2) is 0:
            word = "odd"
        else:
            word = "even"
        return render_template('6-number_odd_or_even.html', nb=n, word=word)

if __name__ == '__main__':
    app.run()
