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

QUOTES = [
    (
        "You don't have to be a mathematician to have a feel for numbers.",
        "John Forbes Nash, Jr."
    ),
    (
        "Just because we can't find a solution, it doesn't mean there isn't one.",
        "Andrew Wiles"
    ),
    (
        "Mathematics is like love; a simple idea, but it can get complicated.",
        "Anonymous"
    ),
    (
        "The only way to learn mathematics is to do mathematics.",
        "Paul R. Halmos"
    ),
    (
        "Mathematics is the music of reason.",
        "James Joseph Sylvester"
    ),
    (
        "Go down deep enough into anything and you will find mathematics.",
        "Dean Schlicter"
    ),
    (
        "Nature is written in mathematical language.",
        "Galileo Galilei"
    ),
    (
        "Mathematics is a language.",
        "Josiah Willard Gibbs"
    ),
    (
        "Millions saw the apple fall, but Newton asked why.",
        "Bernard Baruch"
    ),
    (
        "If there is a 50-50 chance that something can go wrong, then nine times out of 10 it will.",
        "Paul Harvey"
    ),
    (
        "Mathematics consists of proving the most obvious thing in the least obvious way.",
        "George Pólya"
    ),
    (
        "In mathematics, you don't understand things. You just get used to them.",
        "John von Neumann"
    ),
    (
        "Five out of four people have trouble with fractions.",
        "Steven Wright"
    )
]