import binascii
import hashlib
import os
from datetime import datetime

import jwt
from flask_restful import Resource
from flask import request
from db import db
from models.user import User
from resources.login_resources import LoginResource


class UodateUser(Resource):

    def post(self):
        payload = request.get_json(force=True)
        user_token = payload.get('token')
        user_id = LoginResource.validate_token(self, user_token).get('user_id')

        user = User.query.filter(User.user_id == user_id).first()

        if(user):
            user.email = payload.get('email')
            user.username = payload.get('username')
            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            password_hash = hashlib.pbkdf2_hmac('sha512', payload.get('password').encode('utf-8'), salt, 100000)
            pwdhash = binascii.hexlify(password_hash)
            key = (salt + pwdhash).decode('ascii')
            user.password = key

            return {
                'email': user.email,
                'authToken': jwt.encode({
                    'username': user.username,
                    'user_id': user.user_id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                }, 'secret', algorithm='HS256').decode(),
                'principal': user.username
            }, 200

