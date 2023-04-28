#!/usr/bin/env python3

"""
A basic Flask app with Babel localization and timezone support
"""

from flask import Flask, render_template
from flask_babel import Babel


# Create a Config class for the app
class Config:
    """
    Configuration class for Babel

    Configures the default language to be English ("en")
    and the default timezone to be UTC.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Create an instance of the Flask application
app = Flask(__name__)
# Create an instance of Babel for the app
babel = Babel(app)
# Configure the app using the Config class
app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    Renders the index.html template
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)

