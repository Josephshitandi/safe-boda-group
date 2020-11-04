from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Comment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.column(db.String(1000))
    date = db.Column(db.DateTime, default=datetime.utcnow)

@classmethod
def get_comments(cls):
    comments = Comment.query.filter_by().all()
    return comments