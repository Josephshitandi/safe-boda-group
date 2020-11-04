from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,DateField
from ..models import Comment
from wtforms import StringField, TextAreaField, SubmitField, SelectField, PasswordField,IntegerField
from wtforms.validators import Required, Email, EqualTo, ValidationError


class CommentForm (FlaskForm):
    text = TextAreaField('Leave a comment',validators=[Required()])
    date = DateField
    submit = SubmitField('Submit')

class RiderForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    ridername = StringField('Enter your ridername',validators = [Required()])
    number_plate = StringField('Your number_plate',validators =[Required()])
    motor_model = StringField('Your motor_model',validators =[Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Upload')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_ridername(self,data_field):
        if User.query.filter_by(ridername = data_field.data).first():
            raise ValidationError('That ridername is taken')
        
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about yourself',validators=[Required()])
    submit = SubmitField('Save')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Your Task', validators=[Required()])
    submit = SubmitField('Task')
    
    
class BookForm(FlaskForm):
    first_point = StringField('From')
    second_point = StringField('To')
    mobile = IntegerField('Mobile number')
    payment = SelectField(u'Payment Method', choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa'),('Bank', 'Bank')])
    submit = SubmitField('Submit')

