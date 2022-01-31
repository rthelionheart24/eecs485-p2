"""
Insta485 post view.

URLs include:
/posts/<postid_url_slug>
/posts/?target=URL
/likes/?target=URL
/comments/?target=URL
"""
import arrow
import flask
import insta485
from insta485.views.utility import get_profile_pic


@insta485.app.route('/posts/<postid_url_slug>/')
def show_post(postid_url_slug):
    """Display / route."""
    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        return flask.redirect(flask.url_for('login'))

    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT * FROM posts "
        "WHERE postid == ?",
        (postid_url_slug, )
    )
    post = cur.fetchall()[0]

    cur = connection.execute(
        "SELECT * FROM comments "
        "WHERE postid == ?",
        (post['postid'],)
    )
    post['comments'] = cur.fetchall()
    post['owner_img_url'] = get_profile_pic(post['owner'])
    cur = connection.execute(
        "SELECT owner FROM likes "
        "WHERE postid == ?",
        (post['postid'],)
    )
    liked_users = cur.fetchall()
    post['likes'] = len(liked_users)
    post['liked'] = logname in liked_users
    timestamp = arrow.get(post['created'])
    post['created'] = arrow.now().humanize(timestamp)

    context = {"logname": logname, "post": post}
    return flask.render_template("post.html", **context)



@insta485.app.route('/posts/?target=URL')
def edit_post(url):
    """Display / route."""


@insta485.app.route('/likes/?target=URL')
def edit_like(url):
    """Display / route."""


@insta485.app.route('/comments/?target=URL')
def edit_comment(url):
    """Display / route."""

