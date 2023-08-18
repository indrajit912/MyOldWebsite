"""
Flask App Configuration

This module defines configuration settings for the Flask web application.

"""
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get("INDRAJITS_BOT_EMAIL_ID")  # Your Gmail email address
MAIL_PASSWORD = os.environ.get("INDRAJITS_BOT_APP_PASSWORD")  # Your Gmail password or app-specific password
MAIL_DEFAULT_SENDER = os.environ.get("INDRAJITS_BOT_EMAIL_ID")  # Default sender email address