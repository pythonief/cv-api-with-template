"""
Template models file for a blueprint.
Hints:
    - The dataclass import utilitie is the built-in functionality from python to replace 
    the Flask-Marshmallow extension. It needs you declare metadata attributes before initialization
    and the decorator @dataclass before the class declaration
"""

# Import utilities
from dataclasses import dataclass


# Import extensions
from myapp.extensions import db

"""
MODEL CLASSES DB
"""

MAX_STRING_LENGHT = 80
PASSWORD_MAX_LENGHT = 14


@dataclass
class User(db.Model):
    # Meta attributes for dataclass decorator
    id: int
    fullname: str
    email: str
    is_admin: bool

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(MAX_STRING_LENGHT),
                         unique=True, nullable=False)
    email = db.Column(db.String(MAX_STRING_LENGHT),
                      unique=True, nullable=False)
    password = db.Column(db.String(PASSWORD_MAX_LENGHT), nullable=False)
    is_admin = db.Column(db.Boolean)

    def __init__(self, fullname: str, email: str, password: str, is_admin: bool = False):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.is_admin = is_admin
