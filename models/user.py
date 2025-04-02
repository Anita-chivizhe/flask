import uuid

from flask import UserMixin

from extensions import db


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.username,
            "password": self.password,
        }
