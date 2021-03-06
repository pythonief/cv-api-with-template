"""
View Classes for the API. We recommend to use MethodView inherited classes
"""

# Import flask utilities
from flask.helpers import url_for
from flask.views import MethodView
from flask.json import jsonify
from flask import request
from flask import Response

# Import extensions
import requests
from werkzeug.security import generate_password_hash

# Import models
from .models import User

"""
MethodView Class
"""


class UserAPI(MethodView):

    def get(self, user_id=None):
        if user_id is None:
            list_users = User.get_all()
            if list_users:
                return jsonify(list_users), 200
        else:
            user = User.get_entity_by_id(user_id)
            if user:
                return jsonify(user), 200
        return '', 204

    def post(self):
        data = request.get_json()
        if data:
            fullname = data.get('fullname', None)
            email = data.get('email', None)
            password = data.get('password', None)
            user, errors = User.create_instance(fullname, email, password)
            if user:
                user.save()

                user_serialized = jsonify(user).data

                response = Response(user_serialized)
                response.content_type = 'application/json'
                response.headers['Location'] = user.get_url()
                response.status = 200
                return response
            else:
                return jsonify(errors), 400
        else:
            return {
                'message': 'body is empty'
            }, 400

    def delete(self, user_id: int):
        user: User = User.get_entity_by_id(user_id)
        if user:
            user.delete()
            return '', 204
        else:
            return '', 400

    def put(self, user_id: int):
        user: User = User.get_entity_by_id(user_id)
        data = request.get_json()
        if not user and data:
            response = requests.post(url_for(
                'users.users'), json=data, headers=request.headers, cookies=request.cookies)
            return (response.content, response.status_code, response.headers.items())
        if not data:
            return jsonify({
                'message': 'body is empty'
            }), 400
        new_data = {}
        fullname = data.get('fullname', None)
        email = data.get('email', None)
        password = data.get('password', None)
        if fullname:
            new_data['fullname'] = fullname
        if email:
            new_data['email'] = email
        if password:
            new_data['password'] = password
        print(new_data)
        updated_user = user.update_instance(new_data)
        if updated_user:
            updated_user.save()
            return '', 200
        return '', 400
