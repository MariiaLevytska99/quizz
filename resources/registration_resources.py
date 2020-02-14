from flask_restful import Resource
from flask import request
import os
import hashlib, uuid
from db import db
from models.user import User

class RegistrationResource(Resource):
    def put(self):
        payload = request.get_json(force=True)
        password = payload.get('password')

        salt = uuid.uuid4()
        key = hashlib.sha512(password + str(salt))

        new_user = User(username = payload.get('username'), email = payload.get('email'),
                        password = key, salt = salt)

        db.session.add(new_user)
        db.session.commit()

