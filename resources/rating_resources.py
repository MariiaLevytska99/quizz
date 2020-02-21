from flask_restful import Resource
from flask import request
from sqlalchemy import func
from db import db
from models.user import User
from models.user_levels import UserLevels


class RatingResources(Resource):
    def get(self):
        payload = request.get_json(force=True)
        # user_name = payload.get('user')
        # user = User.query.filter(User.username == user_name).first()

        user_ratings = db.session.query(UserLevels.user_id, func.sum(UserLevels.score).label("total_score"))\
            .group_by(UserLevels.user_id).order_by("total_score").all()

        #user_ratings = db.session.execute(query)
        result = []
        for user_rating in user_ratings:
            result.append(
                {
                    "score": str(user_rating.total_score),
                    "user": str(user_rating.user_id)
                }
            )

        return result
