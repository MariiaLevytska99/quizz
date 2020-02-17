from flask_restful import Resource
from flask import request
from db import db
from models.category import Category


class CategoriesResource(Resource):
    def get(self):
        categories = Category.query.all()
        result = []
        for category in categories:
            result.append(
                {
                    'category': category.title
                }

            )

        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_category = Category(title=payload.get('title'))

        db.session.add(new_category)
        db.session.commit()

        return {'message': 'Successfully added'}, 200
