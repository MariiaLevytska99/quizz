from flask_restful import Resource
from flask import request
from db import db
from models.question_answers import QuestionAnswers
from models.answer import Answer


class QuestionAnswersResource(Resource):
    def get(self):
        payload = request.get_json(force=True)
        question_id = payload.get('question')
        answers = QuestionAnswers.query.filter(QuestionAnswers.question_id == question_id).all()
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
        # payload= {[variant1, variant2, variant3 ...]}
        payload = request.get_json(force=True)
        answers = payload.get('answers')
        question_id = payload.get('question')

        if payload is None:
            payload = {}

        for answ in answers:
            answ_id = Answer.query.filter(Answer.text == answ.get('text')).first()
            if answ_id:
                new_answer = QuestionAnswers(question_id=question_id, answer_id=answ_id.answer_id,
                                             correct=answ.get('correct'))
                db.session.add(new_answer)
                db.session.commit()
            else:
                new_answer = Answer(text=answ.get('text'))
                db.session.add(new_answer)
                db.session.commit()
                answ_id = Answer.query.filter(Answer.text == answ.get('text')).first()
                new_answer = QuestionAnswers(question_id=question_id, answer_id=answ_id.answer_id,
                                             correct=answ.get('correct'))
                db.session.add(new_answer)
                db.session.commit()

        return {'message': 'Successfully added'}, 200

    def post(self):
        payload = request.get_json(force=True)
        question_id = payload.get('question')
        selected_answer = payload.get('answer')

        correct = QuestionAnswers.query.filter(QuestionAnswers.question_id == question_id, QuestionAnswers.answer_id ==
                                               selected_answer).first()

        if correct:
            return correct.correct
