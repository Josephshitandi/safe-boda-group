from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class BookForm(FlaskForm):
    firstPoint = StringField('From')
    secondPoint = StringField('To')
    mobile = IntegerField('Mobile number')
    payment = SelectField(u'Payment Method', choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa'),('Bank', 'Bank')])
    submit = SubmitField('Submit')