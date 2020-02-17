from flask_restful import Resource
from flask import request
from db import db
from models.question_answers import QuestionAnswers


class QuestionAnswersResource(Resource):
    def get(self):
        answers = QuestionAnswers.query.all()
        result = []
        for ans in answers:
            result.append(
                {
                    'question': ans.question.text,
                    'answer': ans.answer.text,
                    'correct': ans.correct
                }
            )
        return {'content': result}, 200

    def put(self):
        payload = request.get_json(force=True)
        answers = QuestionAnswers.query.all()

        if payload is None:
            payload = {}

        new_answer = QuestionAnswers(question_id=payload.get('question'), answer_id=payload.get('answer'), correct=payload.get('correct'))

        db.session.add(new_answer)
        db.session.commit()

        return {'message': 'Successfully added'}, 200