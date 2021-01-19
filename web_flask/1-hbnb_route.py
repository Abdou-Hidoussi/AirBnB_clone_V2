#!/usr/bin/python3
""" Task 0 """
from flask import Flask


app = Flask(__name__)


@app.route('/')
def rootdict():
    """ Task 0 """
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnbdict():
    """ Task 1 """
    return "HBNB"

if __name__ == '__main__':
    app.run()
