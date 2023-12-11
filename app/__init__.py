"""
Flask Web App Initialization

This module initializes the Flask web application instance, configures it, and imports the routes and extensions.

Attributes:
    app (Flask): The Flask web application instance.
"""
from flask import Flask
from app.errors import errors_bp
from app.blog import blog_bp
from app.teaching import teaching_bp

app = Flask(__name__)

# Register all blueprints
app.register_blueprint(errors_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(teaching_bp)

# Import routes and extensions
from app import routes