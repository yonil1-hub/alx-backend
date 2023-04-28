#!/usr/bin/env python3
"""4-Force locale with URL parameter"""

from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel

# Create a Config class
class Config:
    """Configuration class for Babel.

    It configures the default language to be English
    and the default timezone to be UTC.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

def get_locale() -> Optional[str]:
    """Returns the best match with our supported languages.

    If the incoming request contains a locale argument
    and it is a valid locale, it returns it.
    Otherwise, it returns the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# Create an instance of Flask
app = Flask(__name__)

# Create an instance of Babel
babel = Babel(app)

# Configure the app with the Config class
app.config.from_object(Config)

# Initialize Babel with the app and the get_locale function
babel.init_app(app, locale_selector=get_locale)

# Create a route for the index page that renders the index.html template
@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """Renders the index.html template."""
    return render_template("4-index.html")

# Run the app only if this file is called directly
if __name__ == "__main__":
    app.run()
