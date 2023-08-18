# Error Handlers for my Website
# Author: Indrajit Ghosh
# Created On: Aug 18, 2023

from flask import Blueprint, render_template
from smtplib import SMTPAuthenticationError, SMTPException

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500

@errors_bp.app_errorhandler(401)
def unauthorized(error):
    """
    Handle cases where users attempt to access a resource that 
    requires authentication but are not authorized to do so.
    """
    return render_template('errors/401.html'), 401


@errors_bp.app_errorhandler(403)
def forbidden(error):
    """
    Handle cases where users attempt to access a resource they 
    don't have permission to access
    """
    return render_template('errors/403.html'), 403

@errors_bp.app_errorhandler(400)
def bad_request(error):
    """
    Handle cases where the user's request is malformed or incorrect.
    """
    return render_template('errors/400.html'), 400

@errors_bp.app_errorhandler(429)
def too_many_requests(error):
    """
    Handle cases where a user has exceeded a rate limit for making requests.
    """
    return render_template('errors/429.html'), 429

# Email-related errors
@errors_bp.app_errorhandler(SMTPAuthenticationError)
def email_auth_error(error):
    return render_template('errors/email_auth_error.html'), 500

@errors_bp.app_errorhandler(SMTPException)
def email_send_error(error):
    return render_template('errors/email_send_error.html'), 500

# Define a catch-all error handler for other exceptions
@errors_bp.app_errorhandler(Exception)
def generic_error(error):
    return render_template('errors/generic_error.html'), 500

