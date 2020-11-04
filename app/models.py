from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Rider.query.get(int(user_id))


class Rider(UserMixin,db.Model):
    __tablename__ = 'riders'

    id = db.Column(db.Integer,primary_key = True)
    ridername = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    number_plate = db.Column(db.String(255),unique = True,index = True)
    motorbike_model = db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def save_rider(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Rider {self.ridername}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Book(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    first_point = db.Column(db.String(255), index=True)
    second_point = db.Column(db.String(255), index=True)
    payment = db.Column(db.String(255), index=True)
    mobile = db.Column(db.String(255), index=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    

    def save_booking(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_bookings(cls, id):
        bookings = Book.query.filter_by(id=id).all()
        return bookings

    @classmethod
    def get_all_bookings(cls):
        bookings = Book.query.order_by('-id').all()
        return bookings

    def __repr__(self):
        return f'Bookings {self._title}'
    
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    riders = db.relationship('Rider',backref = 'role',lazy="dynamic")
    

    def __repr__(self):
        return f'User {self.name}'


