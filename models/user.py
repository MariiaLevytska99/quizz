from db import db


class User(db.Model):
    _tablename_ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(512), unique=False, nullable=False)
    salt = db.Column(db.String(400), unique=False, nullable=False)

    def __init__(self, username, email, password, salt):
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return '<User %r>' % (self.username)