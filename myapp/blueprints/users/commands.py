# CLI Commands
"""
Commans to use in like a cli command
"""

import click
from myapp.extensions.db import db
from werkzeug.security import generate_password_hash


@click.command('createsuperuser')
@click.argument('fullname')
@click.argument('email')
@click.argument('password')
def createsuperuser(fullname, email, password):
    """
    Create a superuser via cli avoid common users can create a superuser account in the users api
    """
    if password:
        from run import app
        from .models import User
        with app.app_context():
            password = generate_password_hash(password, method='sha256')
            user = User.query.filter_by(email=email).first()

            if user:
                raise Exception('User email exists')

            new_user = User(fullname=fullname, email=email,
                            password=password, is_admin=True)
            db.session.add(new_user)
            db.session.commit()
            print('ADMIN ROLE CREATED')
