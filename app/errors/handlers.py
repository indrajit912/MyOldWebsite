# Error Handlers for my Website
# Author: Indrajit Ghosh
# Created On: Aug 18, 2023

from . import errors_bp
from flask import render_template
from smtplib import SMTPAuthenticationError, SMTPException


##########################################
#        Page not found!
##########################################
@errors_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

# Create a named route for page_not_found
@errors_bp.route('/page_not_found')
def page_not_found_route():
    return page_not_found(None)


##########################################
#        Internal Server Error!
##########################################
@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500

# Create a named route for internal_server_error
@errors_bp.route('/internal_server_error')
def internal_server_error_route():
    return internal_server_error(None)

##########################################
#        Unauthorize!
##########################################
@errors_bp.app_errorhandler(401)
def unauthorized(error):
    """
    Handle cases where users attempt to access a resource that 
    requires authentication but are not authorized to do so.
    """
    return render_template('errors/401.html'), 401

# Create a named route for unauthorized
@errors_bp.route('/unauthorized')
def unauthorized_route():
    return unauthorized(None)
    
##########################################
#        Forbidden!
##########################################
@errors_bp.app_errorhandler(403)
def forbidden(error):
    """
    Handle cases where users attempt to access a resource they 
    don't have permission to access
    """
    return render_template('errors/403.html'), 403

# Create a named route for forbidden
@errors_bp.route('/forbidden')
def forbidden_route():
    return forbidden(None)

##########################################
#        Bad request!
##########################################
@errors_bp.app_errorhandler(400)
def bad_request(error):
    """
    Handle cases where the user's request is malformed or incorrect.
    """
    return render_template('errors/400.html'), 400

# Create a named route for bad_request
@errors_bp.route('/bad_request')
def bad_request_route():
    return bad_request(None)

##########################################
#        Too many requests!
##########################################
@errors_bp.app_errorhandler(429)
def too_many_requests(error):
    """
    Handle cases where a user has exceeded a rate limit for making requests.
    """
    return render_template('errors/429.html'), 429

# Create a named route for too_many_requests
@errors_bp.route('/too_many_requests')
def too_many_requests_route():
    return too_many_requests(None)

##########################################
#      Email authorization error!
##########################################
@errors_bp.app_errorhandler(SMTPAuthenticationError)
def email_auth_error(error):
    return render_template('errors/email_auth_error.html'), 500

# Create a named route for email_auth_error
@errors_bp.route('/email_auth_error')
def email_auth_error_route():
    return email_auth_error(None)

##########################################
#        Email sending error!
##########################################
@errors_bp.app_errorhandler(SMTPException)
def email_send_error(error):
    return render_template('errors/email_send_error.html'), 500

# Create a named route for email_send_error
@errors_bp.route('/email_send_error')
def email_send_error_route():
    return email_send_error(None)

#######################################################################
#      A catch-all error handler for other exceptions!
########################################################################
@errors_bp.app_errorhandler(Exception)
def generic_error(error):
    return render_template('errors/generic_error.html'), 500

# Create a named route for generic errors
@errors_bp.route('/generic_error')
def generic_error_route():
    return generic_error(None)

