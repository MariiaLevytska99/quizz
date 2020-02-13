from flask_restful import Resource
from flask import request
from db import db
from models.user_levels import UserLevels


class UserLevelsResource(Resource):
    def get(self):
        user_levels = UserLevels.query.all()
        result = []
        for us_lev in user_levels:
            result.append(
                {
                    'username': us_lev.user.username,
                    'category': us_lev.level.category.title,
                    'level': us_lev.level.level_number,
                    'score': us_lev.score
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)
        user_levels = UserLevels.query.all()

        if payload is None:
            payload = {}

        new_user_level = UserLevels(user_id=payload.get('user'), level_id=payload.get('level'), score=payload.get('score'))


        db.session.add(new_user_level)
        db.session.commit()

        return {'message': 'Successfully added'}, 200