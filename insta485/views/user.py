"""
Insta485 user view.

URLs include:
/users/<user_url_slug>/
"""
import flask
import insta485
from insta485.views.utility import get_following_list, get_followers_list, get_profile_pic, user_exists_in_database, follows


@insta485.app.route('/users/<user_url_slug>/')
def show_user(user_url_slug):
    """Display / route."""
    if not user_exists_in_database(user_url_slug):
        flask.abort(404)

    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        flask.redirect(flask.url_for('/accounts/login'))

    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT fullname FROM users "
        "WHERE username == ?",
        (user_url_slug, )
    )
    fullname = cur.fetchall()[0]['fullname']

    cur = connection.execute(
        "SELECT postid, filename FROM posts "
        "WHERE owner == ?",
        (user_url_slug, )
    )
    posts = cur.fetchall()

    # Add database info to context
    context = {"logname": logname, "username": user_url_slug,
               "logname_follows_username": follows(logname, user_url_slug),
               "fullname": fullname,
               "following": len(get_following_list(user_url_slug)),
               "followers": len(get_followers_list(user_url_slug)),
               "total_posts": len(posts), "posts": posts}
    return flask.render_template("user.html", **context)


@insta485.app.route('/users/<user_url_slug>/followers')
def show_followers(user_url_slug):
    """Display / route."""
    if not user_exists_in_database(user_url_slug):
        flask.abort(404)

    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        flask.redirect(flask.url_for('/accounts/login'))

    followers_list = get_followers_list(user_url_slug)
    followers = []
    for follower in followers_list:
        dic = {'username': follower, 'user_img_url': get_profile_pic(follower),
               'logname_follows_username': follows(logname, follower)}
        followers.append(dic)

    context = {"logname": logname, "followers": followers}
    return flask.render_template("followers.html", **context)


@insta485.app.route('/users/<user_url_slug>/following')
def show_following(user_url_slug):
    """Display / route."""
    if not user_exists_in_database(user_url_slug):
        flask.abort(404)

    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        flask.redirect(flask.url_for('/accounts/login'))

    following_list = get_following_list(user_url_slug)
    following = []
    for follow in following_list:
        dic = {'username': follow, 'user_img_url': get_profile_pic(follow),
               'logname_follows_username': follows(logname, follow)}
        following.append(dic)

    context = {"logname": logname, "following": following}
    return flask.render_template("following.html", **context)


@insta485.app.route('/following/?target=URL')
def edit_follow(url):
    """Display / route."""
