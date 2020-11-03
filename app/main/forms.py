from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
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
