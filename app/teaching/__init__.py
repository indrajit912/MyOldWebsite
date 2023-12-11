from flask import Blueprint

teaching_bp = Blueprint(
    'teaching', 
    __name__, 
    url_prefix='/teaching', 
    template_folder="templates", 
    static_folder="static"
)

from . import routes