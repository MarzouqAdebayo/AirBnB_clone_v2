#!/usr/bin/python3
"""
Module "2-c_route.py"
"""
from flask import Flask, render_template


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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Function c_text that handles "/c/<argument>" route
    returns value of text argument
    """
    return 'C ' + text.replace('_', ' ')


@app.route("/python", defaults={'text', 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Function python_text that handles "/python/<argument>" route
    returns value of text argument
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def accept_number(n):
    """
    Function accept_number that handles "/number/<n>" route
    returns value of number if int
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Function number_template that handles "/number_template/<n>" route
    returns a html template only if n is an integer
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
