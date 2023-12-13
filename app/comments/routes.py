from . import comments_bp
from app.models.comments import Comment
from app.database import db

from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta, timezone


def convert_utc_to_ist(utc_datetime_str):
    """
    Convert a UTC datetime string to Indian Standard Time (IST) format.

    Args:
        utc_datetime_str (str): A string representing a UTC datetime in the format '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: A string representing the datetime in IST format, e.g., 'Dec 13, 2023 07:06 AM IST'.

    Example:
        >>> convert_utc_to_ist('2023-12-13 07:06:16')
        'Dec 13, 2023 07:06 AM IST'
    """
    # Convert string to datetime object
    utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%d %H:%M:%S")

    # Define UTC and IST timezones
    utc_timezone = timezone.utc
    ist_timezone = timezone(timedelta(hours=5, minutes=30))

    # Convert UTC datetime to IST
    ist_datetime = utc_datetime.replace(tzinfo=utc_timezone).astimezone(ist_timezone)

    # Format datetime in the desired string format
    formatted_datetime = ist_datetime.strftime("%b %d, %Y %I:%M %p IST")

    return formatted_datetime

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

@comments_bp.route('/allcomments')
def allcomments():
    # Fetch all comments from the database
    comments = Comment.query.all()

    # Render the template with the comments
    return render_template('all_comments.html', comments=comments)