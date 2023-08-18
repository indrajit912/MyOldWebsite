"""
Flask Web App Initialization

This module initializes the Flask web application instance, configures it, and imports the routes and extensions.

Attributes:
    app (Flask): The Flask web application instance.
"""
from flask import Flask
from .errors.handlers import errors_bp

app = Flask(__name__)

# Register the error blueprints
app.register_blueprint(errors_bp)

# Import routes and extensions
from app import routes