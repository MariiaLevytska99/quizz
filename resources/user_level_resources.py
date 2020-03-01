from flask_restful import Resource
from flask import request
from db import db
from models.user_levels import UserLevels
from models.level import Level
from models.category import Category
from models.user import User
from models.user_levels import UserLevels
from resources.login_resources import LoginResource


class UserLevelsResource(Resource):
    def get(self, user_id, level_id):

        score = UserLevels.query.filter(UserLevels.user_id == user_id, UserLevels.level_id == level_id).first()
        return score

        # token = request.get_json(force=True).get('token')
        # if not token:
        #     return 404
        #
        # decoded_token = LoginResource.validate_token(self,token)
        #
        # if not decoded_token:
        #     return 404;
        # return  decoded_token


# decoded_token        user_levels = UserLevels.query.all()
#         result = []
#         for us_lev in user_levels:
#             result.append(
#                 {
#                     'username': us_lev.user.username,
#                     'category': us_lev.level.category.title,
#                     'level': us_lev.level.level_number,
#                     'score': us_lev.score
#                 }
#             )
#         return {'content': result}, 200

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
        level_number = payload.get('level')
        category_name = payload.get('category')
        score = payload.get('score')
        user = payload.get('user')

        level = Level.query.join(Category).filter(Category.title == category_name, Level.level_number == level_number)\
            .first()
        user_ = User.query.filter(User.username == user).first()

        user_level = UserLevels.query.filter(UserLevels.level_id == level.level_id, UserLevels.user_id == user_.user_id)\
            .first()
        if user_level:
            user_level.score = score
            db.session.add(user_level)
            db.session.commit()
        else:
            new_user_level = UserLevels(user_id=user_.user_id, level_id=level.level_id, score=score)
            db.session.add(new_user_level)
            db.session.commit()


