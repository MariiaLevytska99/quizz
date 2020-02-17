from db import db


class LevelQuestions(db.Model):
    _tablename_ = 'level_questions'

    level_question_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id', name='fk_question_level'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.level_id', name='fk_level_question'), nullable=False)

    question = db.relationship("Question")
    level = db.relationship("Level")

    def __index__(self, question_id, level_id):
        self.question_id = question_id
        self.level_id = level_id

    def __repr__(self):
        return '<Level % r Question %r >' % (self.level_id, self.question_id)