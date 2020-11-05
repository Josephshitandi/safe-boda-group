from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegistrationForm,LoginForm
from ..models import Rider
from .. import db
from ..email import mail_message


@auth.route('/login', methods = ['GET','POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        rider = Rider.query.filter_by(ridername = form.ridername.data).first()
        if rider != None and rider.verify_password(form.password.data):
            login_user(rider,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid ridername or Password')
    return render_template('auth/login2.html', loginform = form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        rider = Rider(email = form.email.data, ridername = form.ridername.data, password = form.password.data)
        rider.save_rider()
        mail_message("Welcome to Safe-Boda","email/welcome_rider",rider.email,rider=rider)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup2.html', r_form = form)
