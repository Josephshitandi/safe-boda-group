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
        first_point = form.first_point.data
        second_point = form.second_point.data
        mobile = form.mobile.data
        payment = form.payment.data

        # Updated booking instance
        new_booking = Book(first_point=first_point,second_point= second_point,mobile = mobile,payment = payment,user_id=current_user.id)

        title='New booking'

        new_booking.save_booking()

        return redirect(url_for('main.new_booking'))

    return render_template('booking.html',form= form, quote=quote)