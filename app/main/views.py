from . import main
from .forms import UpdateProfile,TaskForm,BookForm
from ..models import User,Rider,Book,Comment
from flask import render_template,request,redirect,url_for,abort
from ..request import get_quote
from flask_login import login_required,current_user
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

# @main.route('/rider/<name>')
# def profile2(name):
#     rider = rider.query.filter_by(ridername = name).first()
#     rider_id = current_rider._get_current_object().id
#     if rider is None:
#         abort(404)

#     return render_template("profile/profile2.html", rider = rider)



# @main.route('/rider/<name>/updateprofile', methods = ['POST','GET'])
# @login_required
# def updateprofile2(name):
#     form = UpdateProfile()
#     rider = Rider.query.filter_by(ridername = name).first()
#     if rider == None:
#         abort(404)
#     if form.validate_on_submit():
#         rider.bio = form.bio.data
#         rider.save_rider()
#         return redirect(url_for('.profile2',name = name))
#     return render_template('profile/update2.html',form =form)



# @main.route('/rider/<name>/update/pic',methods= ['POST'])
# @login_required
# def update_pic2(name):
#     rider = Rider.query.filter_by(ridername = name).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         rider.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile2',name=name))	



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    print('user name', user)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/booking/new_booking', methods = ['GET','POST'])
def new_booking():
    quote = get_quote()

    form = BookForm()

    if form.validate_on_submit():
        first_point = form.first_point.data
        second_point = form.second_point.data
        mobile = form.mobile.data
        payment = form.payment.data

        
        new_booking = Book(first_point=first_point,second_point= second_point,mobile = mobile,payment = payment,user_id=current_user.id)

        title='New booking'

        new_booking.save_booking()

        return redirect(url_for('main.new_booking'))

    return render_template('booking.html',form= form, quote=quote)

@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    quote = get_quote()
    comm =Comment.get_comments(id)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title,quote=quote)

@main.route('/new_comment/<int:booking_id>', methods = ['GET','POST'])
@login_required
def new_comment(booking_id):
    quote = get_quote()
    bookings = Book.query.filter_by(id = booking_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment,user_id=current_user.id, booking_id=booking_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New comment'
    return render_template('new_comment.html',title=title,comment_form = form,booking_id=booking_id,quote=quote)

@main.route('/aboutus')
def aboutus():

    return render_template('aboutus.html')


