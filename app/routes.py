"""
Routes and Views

This module defines the routes and views for the Flask web application.

Attributes:
    app (Flask): The Flask web application instance.
"""


from flask import render_template
from app import app

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')

