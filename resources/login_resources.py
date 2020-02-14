import binascii

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

        salt = user.password[:64]
        stored_password = user.password[64:]
        entered_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
        entered_password_hash = binascii.hexlify(entered_password).decode('ascii')

        if user:
            if stored_password == entered_password_hash:
                return 200
            else:
                return 400
        else:
            return 400
