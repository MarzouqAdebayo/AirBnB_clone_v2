#!/usr/bin/python3
"""
Module "1-hbnb_route.py"
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    Function hello_world that handles "/" route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Function hbnb that handles "/hbnb" route
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
