#!/usr/bin/python3
"""
Module "0-hello_route.py" for flask minimal app
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Function hello_world that handles "/" route
    """
    return "<p>Hello, World!</p>"
