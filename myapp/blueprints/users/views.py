"""
View Classes for the API. We recommend to use MethodView inherited classes
"""

# Import flask utilities
from werkzeug.security import gen_salt, generate_password_hash
from flask.views import MethodView
from flask.globals import request
from flask.json import jsonify

# Import extensions
from myapp.extensions import db

# Import models
from .models import User

"""
MethodView Class
"""


class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            list_users = User.query.all()
            if list_users:
                return jsonify(list_users), 200
        else:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return jsonify(user), 200
        return '', 204

    def post(self):
        data = request.get_json()

        fullname = data.get('fullname', None)
        email = data.get('email', None)
        password = data.get('password', None)

        if not password:
            password = gen_salt(14)

        password = generate_password_hash(password, method='sha256')

        user = User.query.filter_by(email=email).first()

        if user:
            return 'email exists', 502

        new_user = User(fullname=fullname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return '', 201

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return '', 200
        else:
            return '', 204

    def put(self, user_id):
        data = request.get_json()
        user = User.query.filter_by(id=user_id)

        if not user:
            return '', 400

        fullname = data.get('fullname', None)
        email = data.get('email', None)
        password = data.get('password', None)

        if not fullname or not email or not password:
            return '', 400

        password = generate_password_hash(password, method='sha256')

        user.fullname = fullname
        user.email = email
        user.password = password
        db.session.add(user)
        db.session.commit()
        return '', 200
