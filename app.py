from flask import Flask
from flask_restful import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
api = Api(app)

from db import db
db.init_app(app)

@@app.route('/')
def printi():
    print("jhgbjhgbj")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
