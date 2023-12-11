"""
Flask Web App Initialization

This module initializes the Flask web application instance, configures it, and imports the routes and extensions.

Attributes:
    app (Flask): The Flask web application instance.
"""
from flask import Flask
from app.errors.handlers import errors_bp
from app.blog.routes import blog_bp

app = Flask(__name__)

# Register all blueprints
app.register_blueprint(errors_bp)
app.register_blueprint(blog_bp)

# Import routes and extensions
from app import routes