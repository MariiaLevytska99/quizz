import binascii

from flask_restful import Resource
from flask import request
import os
import hashlib

from db import db
from sqlalchemy import or_
from models.user import User


class RegistrationResource(Resource):
    def post(self):
        payload = request.get_json(force=True)
        password = payload.get('password')

        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pashas = binascii.hexlify(password_hash)
        key = (salt + pashas).decode('ascii')

        if (User.query.filter(or_(User.email == payload.get('email'), User.username == payload.get('username')))
                .first()):
            return 400

        new_user = User(username=payload.get('username'), email=payload.get('email'), password=key)

        db.session.add(new_user)
        db.session.commit()
