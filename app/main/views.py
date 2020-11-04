from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,TaskForm
from ..models import User,Task

@main.route('/')
def index():
    
    return render_template('index.html', task = Task)

@main.route('/aboutus')
def aboutus():

    return render_template('aboutus.html')
