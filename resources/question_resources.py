from flask_restful import Resource
from flask import request
from db import db
from sqlalchemy.sql import text
from models.question import Question
from models.level import Level
from models.category import Category
from resources.level_questions_resources import LevelQuestionsResource


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
        #payload = {text, type, level_number, category_name}
        payload = request.get_json(force=True)
        questions = Question.query.all()

        if payload is None:
            payload = {}

        new_question = Question(text=payload.get('question'), type_id=payload.get('type'))
        db.session.add(new_question)
        db.session.commit()

        #Add question to the level's questions
        category = payload.get('category')
        level_number = payload.get('level')
        level= Level.query.join(Category).filter(Category.title == category).filter(Level.level_number == level_number).first()
        question = Question.query.order_by(Question.question_id.desc()).first()
        LevelQuestionsResource.put(self, level.level_id, question.question_id);

        return {'message': 'Successfully added'}, 200