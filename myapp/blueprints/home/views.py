"""
View Classes for the API. We recommend to use MethodView inherited classes
"""

# Import flask utilities
from flask.views import View

# Import extensions

# Import models

"""
MethodView Class
"""

class HomeView(View):
    methods = ['GET']
    def dispatch_request(self):
        return "Hello and welcome to the home template for flask API's"