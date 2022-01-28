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


@insta485.app.route('/accounts/logout/')
def logout():
    """Display / route."""


@insta485.app.route('/accounts/create/')
def create():
    """Display / route."""


@insta485.app.route('/accounts/delete/')
def delete():
    """Display / route."""


@insta485.app.route('/accounts/edit/')
def edit():
    """Display / route."""


@insta485.app.route('/accounts/password/')
def password():
    """Display / route."""


@insta485.app.route('/accounts/?target=URL')
def edit_account(url):
    """Display / route."""
