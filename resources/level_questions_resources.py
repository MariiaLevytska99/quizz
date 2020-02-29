from flask_restful import Resource
from flask import request
from db import db
from models.level_questions import LevelQuestions


class LevelQuestionsResource(Resource):
    def get(self):
        payload = request.get_json(force=True)
        level_id = payload.get('level')
        questions = LevelQuestions.query.filter(LevelQuestions.level_id == level_id).all()
        result = []
        for quest in questions:
            result.append(
                {
                    'question': quest.question.text
                }
            )
        return {'content': result}, 200

    def post(self, level_id, question_id):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_question = LevelQuestions(level_id=level_id, question_id=question_id)

        db.session.add(new_question)
        db.session.commit()

        return {'message': 'Successfully added'}, 200