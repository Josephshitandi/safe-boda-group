from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,DateField
from ..models import Comment
from wtforms.validators import DataRequired,Required


class CommentForm (FlaskForm):
    text = TextAreaField('Leave a comment',validators=[Required()])
    date = DateField
    submit = SubmitField('Submit')