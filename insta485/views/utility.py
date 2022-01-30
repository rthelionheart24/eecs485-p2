"""
Insta485 utility.

URLs include:
/uploads/<filename>
"""
import flask
import insta485


@insta485.app.route('/uploads/<filename>')
def download_file(filename):
    return flask.send_from_directory(
        insta485.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )


def get_following_list(username):
    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT * FROM following "
        "WHERE username1 == ?",
        (username,)
    )
    following_list = [d['username2'] for d in cur.fetchall()]
    return following_list


def get_followers_list(username):
    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT * FROM following "
        "WHERE username2 == ?",
        (username,)
    )
    followers_list = [d['username1'] for d in cur.fetchall()]
    return followers_list


def get_profile_pic(username):
    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT filename FROM users "
        "WHERE username == ?",
        (username, )
    )
    return cur.fetchall()[0]['filename']


def user_exists_in_database(username):
    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT * FROM users "
        "WHERE username == ?",
        (username,)
    )
    return len(cur.fetchall()) != 0


def follows(username1, username2):
    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT * FROM following "
        "WHERE (username1, username2) == (?, ?)",
        (username1, username2)
    )
    return len(cur.fetchall()) != 0
