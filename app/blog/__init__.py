from flask import Blueprint

blog_bp = Blueprint(
    'blog', 
    __name__, 
    url_prefix='/blog', 
    template_folder="templates", 
    static_folder="static"
)

from . import routes