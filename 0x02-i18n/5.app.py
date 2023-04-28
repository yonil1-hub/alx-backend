#!/usr/bin/env python3
"""Mock a logging in user"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

# Define a configuration class for Babel
class Config:
    """
    The supported languages are English and French.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Define a function that returns the best match of supported languages
def get_locale():
    """Returns the best match of supported languages based on the request headers.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)

# Define a mock database of users
USERS = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Create a Flask app instance
app = Flask(__name__)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

# Set the app's configuration with the Config class
app.config.from_object(Config)

# Define a function that returns a user dictionary or None
def get_user():
    """Returns a user dictionary or None if the ID cannot be found.
    """
    login_id = request.args.get("login_as")
    if login_id is None:
        return None
    return USERS.get(int(login_id))

# Define a before_request function that sets a global user
@app.before_request
def before_request():
    """Sets a global user object for the Flask application.
    """
    g.user = get_user()

# Define a route for the index page
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Renders the index.html template.
    """
    return render_template("5-index.html")

# Run the app if this file is called directly
if __name__ == "__main__":
    app.run()
