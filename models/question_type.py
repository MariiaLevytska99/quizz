from db import db


class QuestionType(db.Model):
    _tablename_ = 'question_type'

    type_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    type = db.Column(db.String(100), nullable=False)

    def __index__(self, type):
        self.type = type

    def __repr__(self):
        return '<Question type is %r>' % (self.type)