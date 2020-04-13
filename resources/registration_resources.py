import binascii
import smtplib
import ssl

from flask_restful import Resource
from flask import request
import os
import hashlib

from config import Config
from db import db
from sqlalchemy import or_
from models.user import User
from resources.email_resource import send_email


class RegistrationResource(Resource):
    def post(self):
        payload = request.get_json(force=True)
        password = payload.get('password')

        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(password_hash)
        key = (salt + pwdhash).decode('ascii')

        if (User.query.filter(or_(User.email == payload.get('email'), User.username == payload.get('username')))
                .first()):
            return 400

        new_user = User(username=payload.get('username'), email=payload.get('email'), password=key)

        db.session.add(new_user)
        db.session.commit()



