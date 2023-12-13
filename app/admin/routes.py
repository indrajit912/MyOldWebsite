# Admin related routes
# Author: Indrajit Ghosh
# Created On: Dec 12, 2023

from . import admin_bp
from app.models.comments import Comment
from app.models.users import User
from app.database import db

from flask import render_template, url_for, request, session, redirect, flash
from scripts.utils import convert_utc_to_ist
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from functools import wraps
import random
import hashlib

INDRAJIT_912 = "indrajitghosh912@gmail.com"
    
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

        # Add your authentication logic here
        if username == 'admin' and password == 'password':
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))

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


class AdminDetailsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Admin')

def generate_otp():
    return str(random.randint(100000, 999999))

def sha256_hash(raw_text):
    """Return the hex hash value"""
    hashed = hashlib.sha256(raw_text.encode()).hexdigest()
    return hashed

def send_otp_email(otp):
    # TODO: Write it
    pass

class VerifyOTPForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired(), Length(min=6, max=6, message='OTP must be 6 digits')])
    submit = SubmitField('Verify OTP')


@admin_bp.route('/add_admin')
def add_admin():

    otp = generate_otp()

    # Send OTP via email
    # send_otp_email(otp)
    print(otp)

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
        # Save admin details to the database
        new_admin = User(
            email=form.email.data,
            username=form.username.data,
            fullname=form.fullname.data,
            is_admin=True,
        )

        # Set password for the admin using the set_password method
        new_admin.set_password(form.password.data)

        db.session.add(new_admin)
        db.session.commit()

        flash('New admin added successfully!', 'success')
        return redirect(url_for('admin.login'))

    return render_template('enter_admin_details.html', form=form)


# Define the route to get all admins
@admin_bp.route('/all_admins')
@admin_login_required
def all_admins():
    # Query all users who are admins
    admins = User.query.filter_by(is_admin=True).all()

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