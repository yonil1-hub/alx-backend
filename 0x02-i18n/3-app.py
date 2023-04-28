#!/usr/bin/env python3
"""A simple Flask application with Babel integration."""

from flask import Flask, render_template, request
from flask_babel import Babel

# Create a Config class to hold app configuration data
class Config:
    """App configuration settings."""
    
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Initialize Flask application
app = Flask(__name__)
# Load app configuration data
app.config.from_object(Config)

# Initialize Babel for language localization
babel = Babel(app)

# Define a function to determine the best-matching language
def get_locale():
    """Determine the best-matching language based on the user's browser settings."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# Tell Babel to use the get_locale function to determine the language
babel.localeselector(get_locale)

# Define a route for the index page that renders the index.html template
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Render the index.html template."""
    return render_template("3-index.html")

# Run the app only if this file is called directly
if __name__ == "__main__":
    app.run()
