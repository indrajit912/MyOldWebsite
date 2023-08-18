"""
Flask App Configuration

This module defines configuration settings for the Flask web application.

"""
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

INDRAJITS_BOT_EMAIL_ID = os.environ.get("INDRAJITS_BOT_EMAIL_ID")
INDRAJITS_BOT_EMAIL_PASSWD = os.environ.get("INDRAJITS_BOT_APP_PASSWORD")
INDRAJIT912_GMAIL = os.environ.get("INDRAJIT912_GMAIL")

MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = INDRAJITS_BOT_EMAIL_ID # Your Gmail email address
MAIL_PASSWORD = INDRAJITS_BOT_EMAIL_PASSWD  # Your Gmail password or app-specific password
MAIL_DEFAULT_SENDER = INDRAJITS_BOT_EMAIL_ID  # Default sender email address

GMAIL_SERVER = ['smtp.gmail.com', 587] 