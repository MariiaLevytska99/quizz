from db import db


class Category(db.Model):
    _tablename_ = 'category'

    category_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Category %r>' % (self.title)