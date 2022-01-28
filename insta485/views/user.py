"""
Insta485 user view.

URLs include:
/users/<user_url_slug>/
"""
import flask
import insta485


@insta485.app.route('/users/<user_url_slug>/')
def show_user(user_url_slug):
    """Display / route."""


@insta485.app.route('/users/<user_url_slug>/followers')
def show_followers(user_url_slug):
    """Display / route."""


@insta485.app.route('/users/<user_url_slug>/following')
def show_following(user_url_slug):
    """Display / route."""


@insta485.app.route('/following/?target=URL')
def edit_follow(url):
    """Display / route."""
