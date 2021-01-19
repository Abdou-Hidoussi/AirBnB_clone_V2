#!/usr/bin/python3
""" Task 0 """
from flask import Flask


app = Flask(__name__)


@app.route('/')
def data():
    """ data """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
