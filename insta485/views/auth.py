"""
Insta485 authentication.

URLs include:
/accounts/login/
/accounts/logout/
/accounts/create/
/accounts/delete/
/accounts/edit/
/accounts/password/
/accounts/?target=URL
"""
import flask
import insta485


@insta485.app.route('/accounts/login/')
def login():
    """Display / route."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('show_index'))
    return flask.render_template("login.html")


@insta485.app.route('/accounts/logout/')
def logout():
    """Display / route."""


@insta485.app.route('/accounts/create/')
def create():
    """Display / route."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('edit'))
    return flask.render_template("create.html")


@insta485.app.route('/accounts/delete/')
def delete():
    """Display / route."""
    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        return flask.redirect(flask.url_for('login'))

    context = {'logname': logname}
    return flask.render_template("delete.html", **context)


@insta485.app.route('/accounts/edit/')
def edit():
    """Display / route."""
    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        return flask.redirect(flask.url_for('login'))

    connection = insta485.model.get_db()
    cur = connection.execute(
        "SELECT fullname, email, filename FROM users "
        "WHERE username == ?",
        (logname, )
    )
    dic = cur.fetchall()[0]
    fullname = dic['fullname']
    email = dic['email']
    filename = dic['filename']

    context = {'logname': logname, 'fullname': fullname,
               'email': email, 'filename': filename}
    return flask.render_template("edit.html", **context)


@insta485.app.route('/accounts/password/')
def password():
    """Display / route."""
    if 'username' in flask.session:
        logname = flask.session['logname']
    else:
        return flask.redirect(flask.url_for('login'))

    context = {'logname': logname}
    return flask.render_template("password.html", **context)


@insta485.app.route('/accounts/?target=URL')
def edit_account(url):
    """Display / route."""
