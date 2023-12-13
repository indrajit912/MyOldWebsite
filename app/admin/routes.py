# Admin related routes
# Author: Indrajit Ghosh
# Created On: Dec 12, 2023

from . import admin_bp
from app.models.comments import Comment
from app.models.users import User
from app.database import db
from app.admin.forms import VerifyOTPForm, AdminDetailsForm
from scripts.email_message import EmailMessage
from scripts.utils import convert_utc_to_ist, generate_otp
from config import *

from flask import render_template, url_for, request, session, redirect, flash
from sqlalchemy.exc import IntegrityError

from functools import wraps
from smtplib import SMTPAuthenticationError, SMTPException

    
def admin_login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return view_func(*args, **kwargs)
    return wrapper

@admin_bp.route('/dashboard')
@admin_login_required
def dashboard():
    comments_list = Comment.query.all()

    # Convert UTC datetime to IST format for each comment
    for comment in comments_list:
        comment.created_at = convert_utc_to_ist(comment.created_at.strftime("%Y-%m-%d %H:%M:%S"))

    return render_template('dashboard.html', comments=comments_list)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username exists in the database
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))


@admin_bp.route('/delete_comment/<int:comment_id>', methods=['POST'])
@admin_login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Delete the comment from the database
    db.session.delete(comment)
    db.session.commit()

    flash('Comment deleted successfully', 'success')
    return redirect(url_for('admin.dashboard'))


@admin_bp.route('/add_admin')
def add_admin():

    otp = generate_otp()

    # Render the email template with the provided parameters
    _email_html_text = render_template(
        'email_otp_template.html',
        otp=otp, 
        reason="New Admin Registration",
    )

    # Create the email message
    msg = EmailMessage(
        sender_email_id=INDRAJITS_BOT_EMAIL_ID,
        to=INDRAJIT912_GMAIL,
        subject="Request for New Admin Registration!",
        email_html_text=_email_html_text
    )

    # Send OTP via email
    try:
        # Send the email to Indrajit
        msg.send(
            sender_email_password=INDRAJITS_BOT_EMAIL_PASSWD, 
            server_info=GMAIL_SERVER,
            print_success_status=False
        )
    
    except SMTPAuthenticationError as e:
        # Redirect to the email authentication error page using the error blueprint
        return redirect(url_for('errors.email_auth_error_route'))
    
    
    except SMTPException as e:
        return redirect(url_for('errors.email_send_error_route'))
    
    except:
        # Handle email sending error
        return redirect(url_for('errors.generic_error_route'))


    # Store OTP in session for verification
    session['otp'] = otp

    flash('OTP sent to your email. Check your inbox and enter the OTP to proceed.', 'info')
    return redirect(url_for('admin.verify_otp'))


@admin_bp.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    form = VerifyOTPForm()

    if form.validate_on_submit():
        entered_otp = form.otp.data
        stored_otp = session.get('otp')

        if entered_otp == stored_otp:
            # OTP is valid, proceed to admin details form
            return redirect(url_for('admin.enter_admin_details'))

        flash('Invalid OTP. Please try again.', 'danger')

    return render_template('verify_otp.html', form=form)


@admin_bp.route('/enter_admin_details', methods=['GET', 'POST'])
def enter_admin_details():
    form = AdminDetailsForm()

    if form.validate_on_submit():
        # Check if the username or email already exist in the database
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if existing_user:
            flash('Username or email already exists. Please choose a different one.', 'danger')
            return render_template('enter_admin_details.html', form=form)

        # Save admin details to the database
        new_admin = User(
            email=form.email.data,
            username=form.username.data,
            fullname=form.fullname.data,
            is_admin=True,
        )

        # Set password for the admin using the set_password method
        new_admin.set_password(form.password.data)

        try:
            db.session.add(new_admin)
            db.session.commit()

            flash('New admin added successfully!', 'success')
            return redirect(url_for('admin.login'))

        except IntegrityError:
            db.session.rollback()
            flash('Error adding new admin. Please try again.', 'danger')

    return render_template('enter_admin_details.html', form=form)


# Define the route to get all admins
@admin_bp.route('/all_admins')
@admin_login_required
def all_admins():
    # Query all users who are admins
    admins = User.query.filter_by(is_admin=True).all()

    # Convert UTC datetime to IST format for each comment
    for admin in admins:
        admin.created_at = convert_utc_to_ist(admin.created_at.strftime("%Y-%m-%d %H:%M:%S"))

    # Render the template with the list of admins
    return render_template('all_admins.html', admins=admins)


# Define the route to delete an admin
@admin_bp.route('/delete_admin/<int:admin_id>', methods=['POST'])
@admin_login_required
def delete_admin(admin_id):
    # Query the admin to be deleted
    admin = User.query.get_or_404(admin_id)

    # Delete the admin from the database
    db.session.delete(admin)
    db.session.commit()
    flash('Admin deleted successfully', 'success')

    return redirect(url_for('admin.all_admins'))
