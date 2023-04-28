#!/usr/bin/env python3

"""
A basic Flask app that renders an index.html template
"""

from flask import Flask, render_template


# Create an instance of the Flask application
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    Renders the index.html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
