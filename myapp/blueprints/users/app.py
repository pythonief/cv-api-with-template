# Import flask utilities
from flask import Blueprint
# Import views
from .views import UserAPI

#: Declare the blueprint variable with name and prefix url
users = Blueprint('users', __name__, url_prefix='/users')

# Setiing views
users_view = UserAPI.as_view('user_api')

# Setting url rules
users.add_url_rule(
    rule='/',
    methods=['GET'],
    view_func=users_view,
    defaults={'user_id': None}
)
users.add_url_rule(
    rule='/',
    methods=['POST'],
    view_func=users_view
)
users.add_url_rule(
    rule='/<int:user_id>',
    methods=['GET', 'PUT', 'DELETE'],
    view_func=users_view
)

from .commands import *
