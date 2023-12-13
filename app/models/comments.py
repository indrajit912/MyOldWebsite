from app.database import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(100))
    visitor_email = db.Column(db.String(100))
    comment_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __init__(self, visitor_name, visitor_email, comment_text, created_at=None):
        self.visitor_name = visitor_name
        self.visitor_email = visitor_email
        self.comment_text = comment_text
        self.created_at = created_at or datetime.utcnow()