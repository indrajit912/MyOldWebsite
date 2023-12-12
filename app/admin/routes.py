# Admin related routes
# Author: Indrajit Ghosh
# Created On: Dec 12, 2023

from . import admin_bp
from flask import render_template, url_for, request, session, redirect
import json
from functools import wraps
from config import APP_DATA_DIR

# TODO: Add database.
# TODO: Add delete functionality for comments.

COMMENTS_JSON_FILE = APP_DATA_DIR / 'comments.json'

def save_comments_to_json(comments):
    with open(COMMENTS_JSON_FILE, 'w') as json_file:
        json.dump(comments, json_file, indent=4)

def load_comments_from_json():
    try:
        with open(COMMENTS_JSON_FILE, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
    
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
    comments_list = load_comments_from_json()
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