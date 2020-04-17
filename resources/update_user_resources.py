import binascii
import hashlib
import os

import datetime

import jwt
from flask_restful import Resource
from flask import request
from db import db
from models.user import User
from resources.login_resources import LoginResource


def generate_key(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pashas = binascii.hexlify(password_hash)
    return (salt + pashas).decode('ascii')


class UpdateUser(Resource):

    def post(self):
        payload = request.get_json(force=True)
        user_token = payload.get('token')
        user_id = LoginResource.validate_token(self, user_token).get('user_id')

        user = User.query.filter(User.user_id == user_id).first()

        if user:
            user.email = payload.get('email')
            user.username = payload.get('username')
            user.password = generate_key(payload.get('password'))
            db.session.commit()

            return {
                       'email': user.email,
                       'authToken': jwt.encode({
                           'username': user.username,
                           'user_id': user.user_id,
                           'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                       }, 'secret', algorithm='HS256').decode(),
                       'principal': user.username
                   }, 200


class ResetPassword(Resource):
    def post(self):
        payload = request.get_json(force=True)
        email = payload.get('email')

        user = User.query.filter(User.email == email).first()

        if user:
            user.password = generate_key(payload.get('password'))
            db.session.commit()

            return 200
        else:
            return 404
