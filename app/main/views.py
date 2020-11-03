from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,BookForm
from ..models import Book
from ..request import get_quote
# from flask_login import login_required,current_user
from .. import db,photos
import markdown2




@main.route('/booking/new_booking', methods = ['GET','POST'])
@login_required
def new_booking():
    quote = get_quote()

    form = BookForm()

    if form.validate_on_submit():
        booking= form.description.data
        title=form.booking_title.data

        # Updated booking instance
        new_booking = Book(booking_title=title,description= booking,user_id=current_user.id)

        title='New booking'

        new_booking.save_booking()

        return redirect(url_for('main.new_booking'))

    return render_template('booking.html',form= form, quote=quote)