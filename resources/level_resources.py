from flask_restful import Resource
from flask import request
from db import db
from models.level import Level
from resources.category_levels_resources import LoginResource
from models.user_levels import UserLevels


class LevelsResource(Resource):
    def post(self):
        level_id = request.get_json(force=True).get('level')
        user_token = request.get_json(force=True).get('token')
        score = request.get_json(force=True).get('score')
        user_id = LoginResource.validate_token(self, user_token).get('user_id')
        if user_id:
            user_level = UserLevels.query.filter(UserLevels.level_id == level_id, UserLevels.user_id == user_id).first()
            if user_level:
                if user_level.score < score:
                    user_level.score = score
                    db.session.commit()

            return 200

    def get(self):
        levels = Level.query.all()
        result = []
        for level in levels:
            result.append(
                {
                    'level': level.level_number,
                    "category": level.category.title,
                    'points_need': level.points_to_unlock
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_level = Level(level_number=payload.get('level_number'), category_id=payload.get('category'),
                          points_to_unlock=payload.get('points_need'))

        db.session.add(new_level)
        db.session.commit()

        return {'message': 'Successfully added'}, 200
