from db import db


class Question(db.Model):
    _tablename_ = 'question'

    question_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    type_id = db.Column(db.Integer, db.ForeignKey('question_type.type_id', name='fk_question_type'),
                              nullable=False)
    text = db.Column(db.Text, nullable=False)

    type = db.relationship("QuestionType")

    def __index__(self, text, type_id):
        self.type_id = type_id
        self.text = text

    def __repr__(self):
        return '<Question % r Type %r >' % (self.text, self.type_id)
