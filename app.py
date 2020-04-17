from flask import Flask, abort, redirect, request
from flask_restful import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
api = Api(app)

from db import db
db.init_app(app)

from flask_mail import Mail
mail = Mail(app)

from resources.user_resources import UsersResource
from resources.category_resources import CategoriesResource
from resources.level_resources import LevelsResource
from resources.user_level_resources import UserLevelsResource
from resources.answer_resources import AnswersResource
from resources.question_resources import QuestionsResource
from resources.question_type_resources import QuestionTypesResource
from resources.question_answers_resources import QuestionAnswersResource
from resources.registration_resources import RegistrationResource
from resources.login_resources import LoginResource
from resources.category_levels_resources import CategoryLevelsResource
from resources.level_questions_resources import LevelQuestionsResource
from resources.rating_resources import RatingResources
from resources.update_user_resources import UpdateUser
from resources.update_user_resources import ResetPassword

api.add_resource(UsersResource, '/api/users')
api.add_resource(CategoriesResource, '/api/categories')
api.add_resource(LevelsResource, '/api/levels')
api.add_resource(UserLevelsResource, '/api/user/levels')
api.add_resource(AnswersResource, '/api/user/answers')
api.add_resource(QuestionsResource, '/api/questions')
api.add_resource(QuestionTypesResource, '/api/questions/types')
api.add_resource(QuestionAnswersResource, '/api/questions/answers')
api.add_resource(RegistrationResource, '/api/registration')
api.add_resource(LoginResource, '/api/login')
api.add_resource(CategoryLevelsResource, '/api/category/levels')
api.add_resource(LevelQuestionsResource, '/api/level/questions')
api.add_resource(RatingResources, '/api/users/rating')
api.add_resource(UpdateUser, '/api/user/update')
api.add_resource(ResetPassword, '/api/login/reset')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

