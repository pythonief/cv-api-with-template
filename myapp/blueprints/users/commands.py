# CLI Commands
"""
Commans to use in like a cli command
"""

import click
from werkzeug.security import generate_password_hash
from myapp.extensions import db
from .app import users
from .models import User


@users.cli.command('createsuperuser')
@click.argument('fullname')
@click.argument('email')
@click.argument('password')
def createsuperuser(fullname, email, password):
    """
    Create a superuser via cli avoid common users can create a superuser account in the users api
    """
    if password:

        password = generate_password_hash(password, method='sha256')
        user = User.query.filter_by(email=email).first()

        if user:
            raise Exception('User email exists')

        new_user = User(fullname=fullname, email=email,
                        password=password, is_admin=True)
        db.session.add(new_user)
        db.session.commit()
        print('ADMIN ROLE CREATED')
