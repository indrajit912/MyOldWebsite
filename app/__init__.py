"""
Flask Web App Initialization

This module initializes the Flask web application instance, configures it, and imports the routes and extensions.

Attributes:
    app (Flask): The Flask web application instance.
"""
from flask import Flask
from secrets import token_hex
from app.errors import errors_bp
from app.blog import blog_bp
from app.teaching import teaching_bp
from app.comments import comments_bp
from app.admin import admin_bp
from .database import db


app = Flask(__name__)

# Set a secure and random secret key
app.secret_key = token_hex(16)

# Register all blueprints
app.register_blueprint(errors_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(teaching_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(admin_bp)

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Import routes and extensions
from app import routes