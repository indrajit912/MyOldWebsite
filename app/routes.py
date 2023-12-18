"""
Routes and Views

This module defines the routes and views for the Flask web application.

Author: Indrajit Ghosh
Created on: Aug 12, 2023

Attributes:
    app (Flask): The Flask web application instance.
"""

from app import app
from flask import render_template, request, url_for, redirect

from pathlib import Path
from smtplib import SMTPAuthenticationError, SMTPException

from config import *
from scripts.email_message import EmailMessage
from scripts.utils import convert_zip_to_base64


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


@app.route('/index_mobile/')
def index_mobile():
    return render_template('index_mobile.html')


######################################################################
#                       Research
######################################################################
@app.route('/research/')
def research():
    return render_template('research.html')


######################################################################
#                       Miscellaneous
######################################################################
@app.route('/misc/')
def misc():
    isi_reg_zip_path = Path(__file__).parent.absolute() / 'static' / 'others' / 'isi_reg_form.zip'
    amsart_template_zip_path = Path(__file__).parent.absolute() / 'static' / 'others' / 'amsart_template_indrajit.zip'
    formal_letter_template_zip_path = Path(__file__).parent.absolute() / 'static' / 'others' / 'formal-letter-template-Indrajit.zip'
    
    return render_template(
        'misc.html', 
        convert_zip_to_base64=convert_zip_to_base64,
        isi_reg_zip_path=isi_reg_zip_path,
        amsart_template_zip_path=amsart_template_zip_path,
        formal_letter_template_zip_path=formal_letter_template_zip_path
    )


######################################################################
#                       Timeline
######################################################################
@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

######################################################################
#                       Photos
######################################################################
@app.route('/photos/')
def photos():
    return render_template('photos.html')

######################################################################
#                       CV
######################################################################
@app.route('/cv/')
def cv():
    return render_template('cv.html')

######################################################################
#                       Coming Soon!
######################################################################
@app.route('/coming_soon/')
def coming_soon():
    return render_template('coming_soon.html')

######################################################################
#                       Contact Me!
######################################################################
@app.route('/contact/', methods=['GET', 'POST'])
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
            return redirect(url_for('errors.email_auth_error_route'))
        
        
        except SMTPException as e:
            return redirect(url_for('errors.email_send_error_route'))
        
        except:
            # Handle email sending error
            return redirect(url_for('errors.generic_error_route'))


    return render_template('contact.html')

###########################################################
#               Test route
###########################################################
@app.route('/devtest/')
def devtest():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    return f"User IP: {user_ip}"
