from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from . import main





@main.route('/create_new', methods = ['POST','GET'])
def post_comment(id):
    ''' 
    function to post comments 
    '''
    form = CommentForm()
    title = 'post comment'
    comment = Comment.query.filter_by().first()

    if comment is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion=opinion, user_id=current_user.id, comment_id=comment.id)
        new_comment.save_comment()
        return redirect(url_for('.comment'))

    return render_template('new_comment.html', comment_form=form, title=title,Comments=comment)
    