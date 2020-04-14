from flask_restful import Resource
from flask import request
from sqlalchemy import func, desc
from db import db
from models.user import User
from models.user_levels import UserLevels


class RatingResources(Resource):
    def get(self):
        users = db.session.query(User.username, User.email, func.sum(UserLevels.score).label("total_score")\
                                 ).join(UserLevels, isouter=True).group_by(User.user_id).\
            order_by(desc("total_score")).all()

        result = []
        position = 1
        for user in users:
            result.append(
                {
                    "score": str(user.total_score),
                    "username": user.username,
                    "email": user.email,
                    "position": position
                }
            )
            position += 1

        return result

