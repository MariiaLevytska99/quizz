from flask_restful import Resource
from flask import request
from db import db
from models.level import Level


class LevelsResource(Resource):
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
