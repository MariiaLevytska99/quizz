from flask_restful import Resource
from flask import request
from db import db
from models.user import User


class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        result = []
        for user in users:
            result.append(
                {
                    'username': user.username,
                    'password': user.password

                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)
        accounts = User.query.all()

        if payload is None:
            payload = {}

        new_user = User(email=payload.get('email'), username=payload.get('username'), password=payload.get('password'))

        for account in accounts:
            if new_user.username == account.username:
                return {}, 400
            if new_user.email == account.email:
                return {}, 400

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'Successfully added'}, 200