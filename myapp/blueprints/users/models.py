"""
Template models file for a blueprint.
Hints:
    - The dataclass import utilitie is the built-in functionality from python to replace 
    the Flask-Marshmallow extension. It needs you declare metadata attributes before initialization
    and the decorator @dataclass before the class declaration
"""

# Import utilities
from .validators import *
from dataclasses import dataclass
from flask import url_for
from werkzeug.security import check_password_hash, gen_salt, generate_password_hash

# Import extensions
from myapp.extensions.db import db
from myapp.extensions.db import SQLBaseModel

"""
MODEL CLASSES DB
"""

MAX_STRING_LENGHT = 80


@dataclass
class User(SQLBaseModel):
    # Meta attributes for dataclass decorator
    id: int
    fullname: str
    email: str
    is_admin: bool

    __tablename__ = 'users'

    fullname = db.Column(db.String(MAX_STRING_LENGHT), nullable=False)
    email = db.Column(db.String(MAX_STRING_LENGHT),
                      unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean)

    def __init__(self, fullname: str, email: str, password: str, is_admin: bool = False):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def save(self):
        super(User, self).save()

    @classmethod
    def get_by_email(cls, email: str):
        user = cls.query.filter_by(email=email).first() or None
        return user

    def update_instance(self, new_data):

        errors = []

        self.fullname = new_data.get('fullname', self.fullname)
        new_email = new_data.get('email', self.email)
        new_password = new_data.get('password', None)

        pass_validated = pass_validator.match(new_password)

        if email_validator.match(new_email):
            self.email = new_email
        else:
            errors.append(email_valid_message)

        if new_password:
            if not pass_validated:
                errors.append(password_valid)
            if not check_password_hash(self.password, new_password) and pass_validated:
                self.password = generate_password_hash(
                    new_password, method='sha256')
            # The password is the same
        if not errors:
            return self
        return errors

    def create_instance(
            fullname: str = None,
            email: str = None,
            password: str = None,
            # TODO: Create a funtionality to manage users with google oauth
            from_oauth: bool = False
    ):
        errors = []

        if not fullname:
            errors.append(f'fullname field missing')
        if not email:
            errors.append(f'email field missing')
        if not password:
            if not from_oauth:
                errors.append(f'password field missing')
            else:
                password = generate_password_hash(
                    gen_salt(14), method='sha256')
        else:
            password = generate_password_hash(password, method='sha256')

        user = User.get_by_email(email)
        if user:
            errors.append('email exists yet')

        if errors:
            return None, errors

        new_user = User(fullname, email, password)
        return new_user, errors

    def get_url(self):
        url = url_for('users.user_GET', user_id=self.id)
        return url
