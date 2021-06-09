# Import flask utilities
from flask import Blueprint

# Import views
from .views import HomeView

#: Declare the blueprint variable with name and prefix url
home = Blueprint('home', __name__, url_prefix='/')

# Setiing views
home_view = HomeView.as_view('home_view')

# Setting url rules
home.add_url_rule(
    rule='/',
    methods=['GET'],
    view_func=home_view,
)
