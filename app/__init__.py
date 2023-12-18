"""
Flask Web App Initialization

This module initializes the Flask web application instance, configures it, and imports the routes and extensions.

Attributes:
    app (Flask): The Flask web application instance.
"""
from flask import Flask

from config import Config

from app.errors import errors_bp
from app.blog import blog_bp
from app.teaching import teaching_bp
from app.comments import comments_bp
from app.admin import admin_bp
from .extensions import db, migrate


def create_app(config_class=Config):
    # Creates an app with specific config class

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the app with db
    db.init_app(app)

    # Initialize the app and db with Flask-Migrate
    migrate.init_app(app, db)

    # Register all blueprints
    app.register_blueprint(errors_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(teaching_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(admin_bp)

    return app


# Create the app
app = create_app()

# Import routes and extensions
from app import routes