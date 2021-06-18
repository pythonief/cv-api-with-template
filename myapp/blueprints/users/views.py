"""
View Classes for the API. We recommend to use MethodView inherited classes
"""

# Import flask utilities
from .models import User
from flask import Response
from flask import request
from flask.json import jsonify
from flask.views import MethodView
from.validators import *

# Import extensions

# Import models

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
                response.status = 201
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
        # Redirect to post method and create a new user registry
        if not user and data:
            return self.post()
        # Get back error response for empty body
        if not data:
            return jsonify({
                'message': 'body is empty'
            }), 400
        # Obtain info from request data
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
        # Validate and modify existing data -> return None or the self user modified
        response = user.update_instance(new_data)
        if isinstance(response, User):
            user.save()
            # Updated
            return '', 200
        # Not updated
        return jsonify(response), 400
