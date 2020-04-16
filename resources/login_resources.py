import binascii
import smtplib
import ssl
import traceback
from urllib.error import HTTPError
from flask_mail import Message
import jwt
from flask_restful import Resource
from flask import request
import hashlib
import datetime
from config import  Config
from app import mail
from config import Config
from models.user import User
from resources.email_resource import send_email

class LoginResource(Resource):
    def post(self):

        payload = request.get_json(force=True)
        username = payload.get('username')
        password = payload.get('password')

        if not username or not password:
            raise NotAuthorized()


        user = User.query.filter(User.username == username).first()

        if not user:
            raise NotAuthorized()

        salt = user.password[:64]
        stored_password = user.password[64:]
        entered_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
        entered_password_hash = binascii.hexlify(entered_password).decode('ascii')

        if user:
            if stored_password == entered_password_hash:
                return {
                    'email': user.email,
                    'authToken': jwt.encode({
                    'username': username,
                    'user_id': user.user_id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                    }, 'secret', algorithm='HS256').decode(),
                    'principal': username
                }

            else:
                return 401
        else:
            return 401




    def generateAuthToken(token):
        try:
            coded_token = token.decode('utf-8')
            decoded = jwt.decode(coded_token, Config.SECRET_KEY, algorithms=['HS256'])
            return 200
        except Exception as ex:
            return ex

    def validate_token(self, user_context) -> dict:

        if not user_context:
            return 303


        try:
            decoded = jwt.decode(user_context, 'secret', algorithms=['HS256'], verify=True)
        except Exception:
            traceback.print_exc()
            return 305

        return decoded


class NotAuthorized(HTTPError):

    def __init__(self):
        super().__init__("Unauthorized", 401)


