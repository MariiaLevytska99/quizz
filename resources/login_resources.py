from flask_restful import Resource
from flask import request
import hashlib, uuid
from models.user import User


class LoginResource(Resource):
    def post(self):
        payload = request.get_json(force=True)
        username = payload.get('username')
        password = payload.get('password')

        user = User.query.filter(User.username == username).first()
        new_key = hashlib.sha512(password + user.salt).hexdigest()
        if user:
            if user.password == new_key:
                return 200
            else:
                return 400
