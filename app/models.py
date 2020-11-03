from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Rider(UserMixin,db.Model):
    __tablename__ = 'rider'

    id = db.Column(db.Integer,primary_key = True)
    ridername = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    number_plate = db.Column(db.String(255),unique = True,index = True)
    motorbike_model = db.Column(db.String(255))