"""
Insta485 explore view.

URLs include:
/explore/
"""
import flask
import insta485
from insta485.views.utility import get_following_list, get_profile_pic


@insta485.app.route('/explore/')
def show_explore():
    """Display / route."""
    connection = insta485.model.get_db()

    logname = 'awdeorio'
    if 'username' in flask.session:
        logname = flask.session['logname']
    following_list = get_following_list(logname)

    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT username FROM users"
    )
    users = [d['username'] for d in cur.fetchall()]
    not_following = []
    for user in users:
        if user not in following_list and user != logname:
            not_following.append({"username": user,
                                  "user_img_url": get_profile_pic(user)})
    context = {"logname": logname, "not_following": not_following}
    return flask.render_template("explore.html", **context)

