from app.extensions import db
from scripts.utils import sha256_hash
from datetime import datetime
import secrets


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    password_salt = db.Column(db.String(32), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, fullname={self.fullname}, email={self.email}, is_admin={self.is_admin}, created_at={self.created_at})"

    def set_password(self, password):
        # Generate a random salt
        salt = secrets.token_hex(16)
        self.password_salt = salt

        # Combine password and salt, then hash
        password_with_salt = password + salt
        hashed_password = sha256_hash(password_with_salt)
        self.password_hash = hashed_password

    def check_password(self, password):
        # Combine entered password and stored salt, then hash and compare with stored hash
        password_with_salt = password + self.password_salt
        hashed_password = sha256_hash(password_with_salt)
        return hashed_password == self.password_hash