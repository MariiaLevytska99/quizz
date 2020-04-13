from flask_restful import Resource
from flask import request
from sqlalchemy import func
from db import db
from models.user import User
from models.user_levels import UserLevels


class RatingResources(Resource):
    def get(self):

        user_ratings = db.session.query(UserLevels.user_id, func.sum(UserLevels.score).label("total_score"))\
            .group_by(UserLevels.user_id).order_by("total_score").all()

        result = []
        position = 1
        for user_rating in user_ratings:
            user = User.query.filter(User.user_id == user_rating.user_id).first()
            result.append(
                {
                    "score": str(user_rating.total_score),
                    "username": user.username,
                    "email": user.email,
                    "position": position
                }
            )
            position += 1

        return result
