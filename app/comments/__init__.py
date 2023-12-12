from flask import Blueprint

comments_bp = Blueprint(
    'comments', 
    __name__, 
    url_prefix='/comments', 
    template_folder="templates", 
    static_folder="static"
)

from . import routes