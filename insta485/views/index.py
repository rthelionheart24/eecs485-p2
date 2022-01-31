"""
Insta485 index (main) view.

URLs include:
/
"""
import arrow
import flask
import insta485
from insta485.views.utility import get_following_list, get_profile_pic


@insta485.app.route('/')
def show_index():
    """Display / route."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))
    logname = flask.session['username']

    following_list = get_following_list(logname)
    following_list.append(logname)

    connection = insta485.model.get_db()
    if len(following_list) == 1:
        cur = connection.execute(
            "SELECT * FROM posts "
            "WHERE owner == ?",
            (logname, )
        )
    else:
        cur = connection.execute(
            "SELECT * FROM posts "
            "WHERE owner IN {} ORDER BY created DESC".format(
                tuple(following_list))
        )

    posts = cur.fetchall()
    for post in posts:
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
        post['created'] = arrow.get(post['created']).humanize()

    context = {"logname": logname, "posts": posts}
    return flask.render_template("index.html", **context)
