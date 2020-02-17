from flask_restful import Resource
from flask import request
from db import db
from models.level_questions import LevelQuestions


class LevelQuestionsResource(Resource):
    def get(self):
        questions = LevelQuestions.query.all()
        result = []
        for quest in questions:
            result.append(
                {
                    'question': quest.question.text,
                    'answer': quest.answer.text
                }
            )
        return {'content': result}, 200

    def put(self, level_id, question_id):
        payload = request.get_json(force=True)
        answers = LevelQuestions.query.all()

        if payload is None:
            payload = {}

        new_question = LevelQuestions(level_id=level_id, question_id=question_id)

        db.session.add(new_question)
        db.session.commit()

        return {'message': 'Successfully added'}, 200