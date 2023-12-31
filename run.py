# MyWebsite
#
# Author: Indrajit Ghosh
# Created on: Aug 12, 2023
#

"""
Run Flask Web App

This script starts the Flask development server to run the web application.

Usage:
    1. flask shell
        >>> from app import db
        >>> db.create_all()

    2. python run.py

Note: Flask Migration
    1. flask db init
    2. flask db migrate -m 'Initial Migrate'
    3. flask db upgrade
    These 2 and 3 you need to do everytime you change some in your db!
"""

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
