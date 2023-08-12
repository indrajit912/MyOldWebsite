# MyWebsite
#
# Author: Indrajit Ghosh
# Created on: Aug 12, 2023
#

"""
Run Flask Web App

This script starts the Flask development server to run the web application.

Usage:
    python run.py

Note:
    Make sure you have the necessary dependencies installed and the virtual environment activated.

"""

from app import app

if __name__ == '__main__':
    app.run(debug=True)
