from db import db


class UserLevels(db.Model):
    _tablename_ = 'user_levels'

    user_level_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', name='fk_user_level'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.level_id', name='fk_level_user'), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship("User")
    level = db.relationship("Level")

    def __index__(self, user_id, level_id, score):
        self.user_id = user_id
        self.level_id = level_id
        self.score = score

    def __repr__(self):
        return '<User % r Level %r Score %r>' % (self.user_id, self.level_id, self.score)