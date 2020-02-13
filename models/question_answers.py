from db import db


class QuestionAnswers(db.Model):
    _tablename_ = 'question_answers'

    question_answer_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id', name='fk_question_answer'), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.answer_id', name='fk_answer_question'), nullable=False)
    correct = db.Column(db.Boolean, nullable=False, default=True)

    question = db.relationship("Question")
    answer = db.relationship("Answer")

    def __index__(self, question_id, answer_id, correct):
        self.question_id = question_id
        self.answer_id = answer_id
        self.correct = correct

    def __repr__(self):
        return '<Question % r Answer %r Correct %r>' % (self.question_id, self.answer_id, self.correct)