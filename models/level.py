from db import db


class Level(db.Model):
    _tablename_ = 'level'

    level_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    level_number = db.Column(db.Integer, nullable=False)
    points_to_unlock = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id', name='fk_level_category'), nullable=False)

    category = db.relationship("Category")

    def __init__(self, level_number, points_to_unlock, category_id):
        self.level_number = level_number
        self.points_to_unlock = points_to_unlock
        self.category_id = category_id

    def __repr__(self):
        return '<Level %r>' % (self.level_number)