from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class BookForm(FlaskForm):
    opinion_title = StringField('Opinion Title')
    description = TextAreaField('Opinion')
    submit = SubmitField('Submit')