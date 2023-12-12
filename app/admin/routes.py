from . import admin_bp
from flask import render_template, url_for, request, session, redirect


@admin_bp.route('/dashboard')
def dashboard():
    # Add authentication check here
    # Example: if user_is_authenticated():
    return render_template('dashboard.html')


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
    return redirect(url_for('admin.login'))