# Routes for blog: /blog
# Author: Indrajit Ghosh
# Created On: Dec 11, 2023

from . import blog_bp
from flask import render_template, redirect, url_for


#####################################
#       Blog Home Page
#####################################
@blog_bp.route('/')
def index():
    return render_template('blog_homepage.html')

###################################
#       Blogs
##################################
@blog_bp.route('/blogpost/<postid>')
def blogpost(postid):
    return render_template('blog_posts/blog_post.html', postid=postid)