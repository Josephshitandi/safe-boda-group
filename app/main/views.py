from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import Rider
from .forms import UpdateProfile
from .. import db,photos




@main.route('/rider/<name>')
def profile(name):
    rider = rider.query.filter_by(ridername = name).first()
    rider_id = current_rider._get_current_object().id
    if rider is None:
        abort(404)

    return render_template("profile/profile.html", rider = rider)



@main.route('/rider/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    rider = Rider.query.filter_by(ridername = name).first()
    if rider == None:
        abort(404)
    if form.validate_on_submit():
        rider.bio = form.bio.data
        rider.save_rider()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)



@main.route('/rider/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    rider = Rider.query.filter_by(ridername = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        rider.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))
