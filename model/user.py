# This file defines the user information and it's rules as it will be stored in the database table

from dataclasses import dataclass

from main import db


@dataclass
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=32), nullable=False, unique=True)
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    password = db.Column(db.String(length=64), nullable=False)
    role = db.Column(db.String(length=32), nullable=False, default="user")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    __table_args__ = (
        db.Index('ix_users_username', db.func.lower(username)),
        db.Index('ix_users_email', db.func.lower(email)),
    )

    def to_response(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }
