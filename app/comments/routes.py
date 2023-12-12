from . import comments_bp
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta, timezone
import json
from config import APP_DATA_DIR

comments_list = []
COMMENTS_JSON_FILE = APP_DATA_DIR / 'comments.json'

def save_comments_to_json(comments):
    with open(COMMENTS_JSON_FILE, 'w') as json_file:
        json.dump(comments, json_file, indent=4)

def load_comments_from_json():
    try:
        with open(COMMENTS_JSON_FILE, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

#####################################
#       Comments Home Page
#####################################
@comments_bp.route('/', methods=['GET', 'POST'])
def index():
    global comments_list
    comments_list = load_comments_from_json()

    if request.method == 'POST':
        visitor_name = request.form.get('visitor_name')
        visitor_email = request.form.get('email')
        comment_text = request.form.get('comment_text')
        
        # Get current datetime in UTC
        utc_now = datetime.now(timezone.utc)
        
        # Convert UTC datetime to IST
        ist = timezone(timedelta(hours=5, minutes=30))
        current_datetime = utc_now.astimezone(ist)
        
        # Format datetime
        formatted_datetime = current_datetime.strftime("%b %d, %Y %I:%M %p IST")
        
        # Create a dictionary to store the comment details
        new_comment = {
            'visitor_name': visitor_name,
            'visitor_email': visitor_email,
            'datetime': formatted_datetime,
            'comment_text': comment_text
        }
        
        comments_list.append(new_comment)
        save_comments_to_json(comments_list)
        return redirect(url_for('comments.index'))

    return render_template('comment_box.html', comments=comments_list)