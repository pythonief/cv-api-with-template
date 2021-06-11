# Import flask utilities
from flask import Blueprint
# Import views
from .views import UserAPI

#: Declare the blueprint variable with name and prefix url
users = Blueprint('users', __name__, url_prefix='/users')

# Setiing views


# Setting url rules
users.add_url_rule(
    rule='/',
    methods=['GET'],
    view_func=UserAPI.as_view('user_ALL'),
    defaults={'user_id': None},
)
users.add_url_rule(
    rule='/',
    methods=['POST'],
    view_func=UserAPI.as_view('user_POST')
)
users.add_url_rule(
    rule='/<int:user_id>',
    methods=['GET'],
    view_func=UserAPI.as_view('user_GET')
)
users.add_url_rule(
    rule='/<int:user_id>',
    methods=['PUT'],
    view_func=UserAPI.as_view('user_PUT')
)
users.add_url_rule(
    rule='/<int:user_id>',
    methods=['DELETE'],
    view_func=UserAPI.as_view('user_DELETE')
)

from .commands import *
