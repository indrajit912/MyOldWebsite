"""
Routes and Views

This module defines the routes and views for the Flask web application.

Author: Indrajit Ghosh
Created on: Aug 12, 2023

Attributes:
    app (Flask): The Flask web application instance.
"""


from flask import render_template, request
from app import app
from config import *

from scripts.email_message import EmailMessage


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

@app.route('/teaching/anal_several_vars_odd_2023.html')
def anal_several_vars_odd_2023_ta():
    return render_template('teaching/anal_several_vars_odd_2023.html')

@app.route('/teaching/comp_anal_odd_sem_2022.html')
def comp_anal_odd_sem_2022_ta():
    return render_template('teaching/comp_anal_odd_sem_2022.html')

@app.route('/teaching/func_anal_even_sem_2021.html')
def func_anal_even_sem_2021_ta():
    return render_template('teaching/func_anal_even_sem_2021.html')

@app.route('/teaching/optimization_odd_sem_2021.html')
def optimization_odd_sem_2021_ta():
    return render_template('teaching/optimization_odd_sem_2021.html')


######################################################################

######################################################################
#                       Research
######################################################################
@app.route('/research')
def research():
    return render_template('research.html')

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
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        msg = EmailMessage(
            sender_email_id=MAIL_DEFAULT_SENDER,
            to="indrajitghosh912@gmail.com",
            subject="New Response",
            email_plain_text=f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        )

        try:
            # Send the email
            msg.send(
                sender_email_password=MAIL_PASSWORD, 
                server_info=['smtp.gmail.com', 587],
                print_success_status=False
            )

            # After processing, you can redirect to a thank-you page.
            return render_template('thank_you.html')
        
        except Exception as e:
            # Handle email sending error
            return f"An error occurred while sending the email."


    return render_template('contact.html')