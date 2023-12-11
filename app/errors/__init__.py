from flask import Blueprint

errors_bp = Blueprint(
    'errors', 
    __name__, 
    url_prefix='/errors', 
    template_folder="templates", 
    static_folder="static"
)

from . import handlers