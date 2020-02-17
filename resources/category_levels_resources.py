from flask_restful import Resource
from flask import request
from db import db
from models.level import Level


class CategoryLevelsResource(Resource):
    def get(self):
        category_id = request.get_json(force=True).get('category')

        levels = Level.query.filter(Level.category_id == category_id).all()

        result = []

        for level in levels:
            result.append(
                {
                    'level': level.level_number,
                    'points to unlock': level.points_to_unlock
                }
            )

        return result
