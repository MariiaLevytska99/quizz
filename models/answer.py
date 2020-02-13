from db import db


class Answer(db.Model):
    _tablename_ = 'answer'

    answer_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    text = db.Column(db.Text, nullable=False)

    def __index__(self, text):
        self.text = text

    def __repr__(self):
        return '<Answer % r >' % (self.text)