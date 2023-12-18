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
from .extensions import db, migrate
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USERNAME, DEBUG


app = Flask(__name__)

# Set a secure and random secret key
app.secret_key = token_hex(16)

app.debug = DEBUG

# Register all blueprints
app.register_blueprint(errors_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(teaching_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(admin_bp)

# Database URI
connection_uri = (
    f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    "?ssl_ca=/etc/ssl/cert.pem"
)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the app with db
db.init_app(app)

# Initialize the app and db with Flask-Migrate
migrate.init_app(app, db)

# Import routes and extensions
from app import routes