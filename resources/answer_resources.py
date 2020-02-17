from flask_restful import Resource
from flask import request
from db import db
from models.answer import Answer


class AnswersResource(Resource):
    def get(self):
        answers = Answer.query.all()
        result = []
        for answer in answers:
            result.append(
                {
                    'answer': answer.text
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_answer = Answer(text=payload.get('answer'))

        db.session.add(new_answer)
        db.session.commit()

        return {'message': 'Successfully added'}, 200