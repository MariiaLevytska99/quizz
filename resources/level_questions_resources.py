from flask_restful import Resource
from flask import request
from db import db
from models.level_questions import LevelQuestions
from models.question_answers import QuestionAnswers


class LevelQuestionsResource(Resource):
    def post(self):
        payload = request.get_json(force=True)
        level_id = payload.get('level')
        questions = LevelQuestions.query.filter(LevelQuestions.level_id == level_id).all()
        result = []
        for quest in questions:
            answersQuery = QuestionAnswers.query.filter(QuestionAnswers.question_id == quest.question.question_id).all()
            if len(answers) > 0:
                answers = []
                for answ in answersQuery:
                    answers.append(
                        {
                            'text': answ.answer.text,
                            'isCorrect': answ.correct
                        }
                    )
                result.append(
                    {
                        'id': quest.question.question_id,
                        'text': quest.question.text,
                        'type': quest.question.type_id,
                        'answers': answers
                    }
                )
        return result, 200

    def get(self, level_id, question_id):
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_question = LevelQuestions(level_id=level_id, question_id=question_id)

        db.session.add(new_question)
        db.session.commit()

        return {'message': 'Successfully added'}, 200