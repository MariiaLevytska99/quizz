from flask_restful import Resource
from flask import request
from db import db
from sqlalchemy.sql import text
from models.question import Question
from models.level import Level
from models.category import Category
from models.level_questions import LevelQuestions
from resources.level_questions_resources import LevelQuestionsResource
from resources.question_answers_resources import QuestionAnswersResource


class QuestionsResource(Resource):
    def get(self):
        #payload = {category, level_number}
        payload = request.get_json(force = True)
        category = payload.get('category')
        level = payload.get('level')
        questions = LevelQuestions.query.join(Level).join(Category).filter(Category.title == category,
                                                                           Level.level_number == level).all()
        result = []
        for quest in questions:
            result.append(
                {
                    'question': quest.question.text,
                    'type': quest.question.type.type,
                    'category': quest.level.category.title
                }
            )
        return {'content': result}, 200

    def post(self):
        #payload = {text, type, level_number, category_name}
        payload = request.get_json(force=True)

        if payload is None:
            payload = {}

        new_question = Question(text=payload.get('question'), type_id=payload.get('type'))
        db.session.add(new_question)
        db.session.commit()

        #Add question to the level's questions
        category = payload.get('category')
        level_number = payload.get('level')
        level= Level.query.filter(Level.category_id == category, Level.level_number == level_number)\
            .first()

        question = Question.query.order_by(Question.question_id.desc()).first()
        LevelQuestionsResource.post(self, level.level_id, question.question_id)

        #Add question answers
        answers = payload.get('answers')
        QuestionAnswersResource.post(self, answers, question.question_id)

        return {'message': 'Successfully added'}, 200