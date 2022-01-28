"""
Insta485 post view.

URLs include:
/posts/<postid_url_slug>
/posts/?target=URL
/likes/?target=URL
/comments/?target=URL
"""
import flask
import insta485


@insta485.app.route('/posts/<postid_url_slug>/')
def show_post(postid_url_slug):
    """Display / route."""


@insta485.app.route('/posts/?target=URL')
def edit_post(url):
    """Display / route."""


@insta485.app.route('/likes/?target=URL')
def edit_like(url):
    """Display / route."""


@insta485.app.route('/comments/?target=URL')
def edit_comment(url):
    """Display / route."""

