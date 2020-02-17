import binascii
import jwt
from flask_restful import Resource
from flask import request
import hashlib
from config import Config
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
                return 404
        else:
            return 404

    def get(token):
        try:
            coded_token = token.decode('utf-8')
            decoded = jwt.decode(coded_token, Config.SECRET_KEY, algorithms=['HS256'])
            return 200
        except Exception as ex:
            return ex
