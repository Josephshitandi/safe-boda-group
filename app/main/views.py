
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,TaskForm
from ..models import User,Task
from flask import render_template,request,redirect,url_for,abort
from .forms import UpdateProfile
from ..request import get_quote
from .. import db,photos
import markdown2


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user
        new_task_object = Task(post=post,user_id=current_user._get_current_object().id,title=title)
        new_task_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_task.html', form = form)		


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Safe Boda  website'
    content = "WELCOME TO SAFE BODA WEBSITE"
    quote = get_quote()

    return render_template('index.html', title = title,content = content,quote = quote)



@main.route('/user/<uname>')
def profile(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, quote=quote)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form, quote=quote)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
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
