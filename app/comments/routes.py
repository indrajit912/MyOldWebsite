from . import comments_bp
from app.models.comments import Comment
from app.database import db
from scripts.utils import convert_utc_to_ist

from flask import render_template, redirect, url_for, request

#####################################
#       Comments Home Page
#####################################
@comments_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        visitor_name = request.form.get('visitor_name')
        visitor_email = request.form.get('email')
        comment_text = request.form.get('comment_text')
        
        # Create a new Comment instance and add it to the database
        new_comment = Comment(
            visitor_name=visitor_name,
            visitor_email=visitor_email,
            comment_text=comment_text
        )

        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('comments.index'))
    
    # Retrieve comments from the database
    comments_list = Comment.query.all()

    # Convert UTC datetime to IST format for each comment
    for comment in comments_list:
        comment.created_at = convert_utc_to_ist(comment.created_at.strftime("%Y-%m-%d %H:%M:%S"))


    return render_template('comment_box.html', comments=comments_list)
