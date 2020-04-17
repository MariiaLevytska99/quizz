from flask_restful import Resource
from flask import request
from db import db
from models.level import Level
from models.user_levels import UserLevels
from resources.login_resources import LoginResource


class UserLevelsResource(Resource):
    def get(self, user_id, level_id):

        score = UserLevels.query.filter(UserLevels.user_id == user_id, UserLevels.level_id == level_id).first()
        if score:
            return score.score
        else:
            return 0

    def put(self):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_user_level = UserLevels(user_id=payload.get('user'), level_id=payload.get('level'), score=payload.get('score'))

        db.session.add(new_user_level)
        db.session.commit()

        return {'message': 'Successfully added'}, 200

    def post(self):
        payload = request.get_json(force=True)
        level_id = payload.get('level')
        user = payload.get('token')
        score = payload.get('score')

        level = Level.query.filter(Level.level_id == level_id).first()

        user_id = LoginResource.validate_token(self, user).get('user_id')
        if user_id:
            user_level = UserLevels.query.filter(UserLevels.level_id == level_id, UserLevels.user_id == user_id).first()
            if user_level:
                if user_level.score < score:
                    user_level.score = score
                    db.session.commit()
            else:
                new_user_level = UserLevels(user_id=user_id, level_id=level.level_id, score=0)
                db.session.add(new_user_level)
                db.session.commit()
            return 200



