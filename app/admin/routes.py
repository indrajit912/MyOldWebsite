# Admin related routes
# Author: Indrajit Ghosh
# Created On: Dec 12, 2023

from . import admin_bp
from flask import render_template, url_for, request, session, redirect
from app.models.comments import Comment
from app.database import db
from scripts.utils import convert_utc_to_ist

import json
from functools import wraps
from config import APP_DATA_DIR

    
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