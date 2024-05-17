#!/usr/bin/python3
"""
Module "7-states.py"
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Function states_list that handles "/states_list" route
    """
    states = storage.all('State').values()
    print(states)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def handle_teardown(self):
    """
    method executed during teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
