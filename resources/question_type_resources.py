from flask_restful import Resource
from flask import request
from db import db
from models.question_type import QuestionType


class QuestionTypesResource(Resource):
    def get(self):
        types = QuestionType.query.all()
        result = []
        for type in types:
            result.append(
                {
                    'type': type.type
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)
        types = QuestionType.query.all()

        if payload is None:
            payload = {}

        new_type = QuestionType(type=payload.get('type'))

        db.session.add(new_type)
        db.session.commit()

        return {'message': 'Successfully added'}, 200