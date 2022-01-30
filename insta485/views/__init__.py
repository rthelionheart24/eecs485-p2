"""Views, one for each Insta485 page."""
from insta485.views.index import show_index
from insta485.views.user import show_user
from insta485.views.user import show_following
from insta485.views.user import show_followers
# from insta485.views.user import edit_follow
# from insta485.views.post import show_post
# from insta485.views.post import edit_post
# from insta485.views.post import edit_like
# from insta485.views.post import edit_comment
# from insta485.views.auth import login
# from insta485.views.auth import logout
# from insta485.views.auth import create
# from insta485.views.auth import delete
# from insta485.views.auth import edit
# from insta485.views.auth import password
# from insta485.views.auth import edit_account
from insta485.views.explore import show_explore
from insta485.views.utility import download_file
