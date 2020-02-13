from flask_restful import Resource
from flask import request
from db import db
from models.question import Question


class QuestiosResource(Resource):
    def get(self):
        questions = Question.query.all()
        result = []
        for question in questions:
            result.append(
                {
                    'question': question.text,
                    'type': question.type.type
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)
        questions = Question.query.all()

        if payload is None:
            payload = {}

        new_question = Question(text=payload.get('question'), type_id=payload.get('type'))

        db.session.add(new_question)
        db.session.commit()

        return {'message': 'Successfully added'}, 200