from flask_restful import Resource
from flask import request
from db import db
from models.level import Level
from resources.login_resources import LoginResource
from resources.user_level_resources import UserLevelsResource

class CategoryLevelsResource(Resource):
    def get(self):
        category_id = request.get_json(force=True).get('category')
        user_token = request.get_json(force=True).get('token')
        user_id = LoginResource.validate_token(self, user_token).get('user_id')
        result = []
        result.append(
            {
            'id': 1,
                'levelNumber': 1,
                'pointsToUnlock': 0,
                'score': 0
            }

        )
        # if(user_id):
        #     levels = Level.query.filter(Level.category_id == category_id).all()
        #     result = []
        #     for level in levels:
        #         score_level = UserLevelsResource.get(self, user_id, level.level_id)
        #         score = 0
        #         if score_level:
        #             score = score_level
        #         result.append(
        #             {
        #                 'id': level.level_id,
        #                 'levelNumber': level.level_number,
        #                 'pointsToUnlock': level.points_to_unlock,
        #                 'score': score
        #             }
        #         )

        return result

    def post(self):
        payload = request.get_json(force=True);
        category_id = payload.get('category');
        level = payload.get('level');
        points = payload.get('points');

        if payload is None:
            payload = {}

        new_category_level = Level(level_number=level, points_to_unlock=points, category_id=category_id);

        db.session.add(new_category_level)
        db.session.commit()

        return {'message': 'Level successfully added'}, 200
