"""
Insta485 index (main) view.

URLs include:
/
"""
import arrow
import flask
import insta485


@insta485.app.route('/')
def show_index():
    """Display / route."""

    # Connect to database
    connection = insta485.model.get_db()

    # Query database
    logname = 'awdeorio'
    if 'username' in flask.session:
        logname = flask.session['logname']

    cur = connection.execute(
        "SELECT * FROM following "
        "WHERE username1 == ?",
        (logname,)
    )
    following_list = [d['username2'] for d in cur.fetchall()]
    following_list.append(logname)

    cur = connection.execute(
        "SELECT * FROM posts "
        "WHERE owner IN {} ORDER BY created DESC".format(tuple(following_list))
    )
    posts = cur.fetchall()

    for post in posts:
        cur = connection.execute(
            "SELECT * FROM comments "
            "WHERE postid == ?",
            (post['postid'], )
        )
        post['comments'] = cur.fetchall()
        cur = connection.execute(
            "SELECT filename FROM users "
            "WHERE username == ?",
            (post['owner'],)
        )
        post['owner_img_url'] = cur.fetchall()[0]['filename']
        cur = connection.execute(
            "SELECT owner FROM likes "
            "WHERE postid == ?",
            (post['postid'], )
        )
        liked_users = cur.fetchall()
        post['likes'] = len(liked_users)
        post['liked'] = logname in liked_users
        timestamp = arrow.get(post['created'])
        post['created'] = arrow.now().humanize(timestamp)

    # Add database info to context
    context = {"logname": logname, "posts": posts}
    return flask.render_template("index.html", **context)
