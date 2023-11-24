"""
Routes and Views

This module defines the routes and views for the Flask web application.

Author: Indrajit Ghosh
Created on: Aug 12, 2023

Attributes:
    app (Flask): The Flask web application instance.
"""


from flask import render_template, request, abort, url_for
from app import app
from config import *
from pathlib import Path
# Import the 'errors' Blueprint
from .errors.handlers import errors_bp

from scripts.email_message import EmailMessage
from scripts.utils import convert_zip_to_base64
from smtplib import SMTPAuthenticationError, SMTPException

import random

######################################################################
#                           Processor Function
######################################################################
# Define the context processor function
# This function make the variables abailable for all routes!
@app.context_processor
def inject_quote():
    quote, quote_source = random.choice(QUOTES)
    return dict(quote=quote, quote_source=quote_source)

######################################################################
#                           Home
######################################################################
@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/index_mobile')
def index_mobile():
    return render_template('index_mobile.html')


######################################################################
#                           Teaching
######################################################################
@app.route('/teaching')
def teaching():
    return render_template('teaching.html')

@app.route('/teaching/isibc/intro_to_cp_even_2024.html')
def intro_to_cp_even_2024():
    return render_template('teaching/isibc/intro_to_cp_even_2024.html')

@app.route('/teaching/isibc/anal_several_vars_odd_2023.html')
def anal_several_vars_odd_2023_ta():
    return render_template('teaching/isibc/anal_several_vars_odd_2023.html')

@app.route('/teaching/isibc/comp_anal_odd_sem_2022.html')
def comp_anal_odd_sem_2022_ta():
    return render_template('teaching/isibc/comp_anal_odd_sem_2022.html')

@app.route('/teaching/isibc/func_anal_even_sem_2021.html')
def func_anal_even_sem_2021_ta():
    return render_template('teaching/isibc/func_anal_even_sem_2021.html')

@app.route('/teaching/isibc/optimization_odd_sem_2021.html')
def optimization_odd_sem_2021_ta():
    return render_template('teaching/isibc/optimization_odd_sem_2021.html')


######################################################################

######################################################################
#                       Research
######################################################################
@app.route('/research')
def research():
    return render_template('research.html')


######################################################################
#                       Miscellaneous
######################################################################
@app.route('/misc')
def misc():
    isi_reg_zip_path = Path(__file__).parent.absolute() / 'static' / 'others' / 'isi_reg_form.zip'
    isi_reg_form_zip_base64 = convert_zip_to_base64(isi_reg_zip_path)
    return render_template('misc.html', isi_reg_form_zip_base64=isi_reg_form_zip_base64)

######################################################################
#                       Blog
######################################################################
@app.route('/blog')
def blog():
    return render_template('blog_listings.html')

@app.route('/blog_posts/blog_post1.html')
def blog_post1():
    return render_template('blog_posts/blog_post1.html')

@app.route('/blog_posts/blog_post2.html')
def blog_post2():
    return render_template('blog_posts/blog_post2.html')

######################################################################
#                       Timeline
######################################################################
@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

######################################################################
#                       Photos
######################################################################
@app.route('/photos')
def photos():
    return render_template('photos.html')

######################################################################
#                       CV
######################################################################
@app.route('/cv')
def cv():
    return render_template('cv.html')

######################################################################
#                       Coming Soon!
######################################################################
@app.route('/coming_soon')
def coming_soon():
    return render_template('coming_soon.html')

######################################################################
#                       Contact Me!
######################################################################
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data and send an email or save the message, etc.
        # You can use Flask-Mail or other libraries for email sending.
        # Get form data from the request object
        name = request.form.get('name')
        email_id = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Process file attachments
        attachments = request.files.getlist('attachment[]')

        # Attach files to the email
        _attachment_paths = []
        for attachment in attachments:
            if attachment:
                _attachment_filename = APP_DATA_DIR / attachment.filename
                attachment.save(_attachment_filename)
                _attachment_paths.append(_attachment_filename)

        # Render the email template with the provided parameters
        _email_html_text = render_template(
            'emails/email_template.html', 
            name=name, 
            subject=subject, 
            message=message, 
            email_id=email_id
        )

        # Create the email message
        msg = EmailMessage(
            sender_email_id=INDRAJITS_BOT_EMAIL_ID,
            to=INDRAJIT912_GMAIL,
            subject="Message from your WebSite!",
            email_html_text=_email_html_text,
            attachments=_attachment_paths
        )


        try:
            # Send the email to Indrajit
            msg.send(
                sender_email_password=INDRAJITS_BOT_EMAIL_PASSWD, 
                server_info=GMAIL_SERVER,
                print_success_status=False
            )

            # Delete the attachments from server
            for attachment_path in _attachment_paths:
                if attachment_path.exists():
                    attachment_path.unlink()


            # After processing, you can redirect to a thank-you page.
            return render_template('thank_you.html')
        
        except SMTPAuthenticationError as e:
            # Redirect to the email authentication error page using the error blueprint
            return errors_bp.email_auth_error(e)
        
        except SMTPException as e:
            return errors_bp.email_send_error(e)
        
        except:
            # Handle email sending error
            return errors_bp.generic_error(e)


    return render_template('contact.html')
