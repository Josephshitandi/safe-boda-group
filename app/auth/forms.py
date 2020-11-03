from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import Rider
from wtforms import StringField,PasswordField,BooleanField,SubmitField


class RiderForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    ridername = StringField('Enter your ridername',validators = [Required()])
    number_plate StringField('Your motor number plate',validators =[Required(),number plate())]
    Motor_model StringField('Your motor model type',validators =[Required(),motor model())]
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Upload')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_ridername(self,data_field):
        if User.query.filter_by(ridername = data_field.data).first():
            raise ValidationError('That ridername is taken')