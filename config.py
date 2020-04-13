import os


class Config(object):
    """
    Base Configuration Class
    Contains all Application Constant
    Defaults
    """
    DEBUG = False
    IS_PRODUCTION = False
    IS_STAGING = False

    db_host = 'dbquiz3.cophtor4sjla.us-east-1.rds.amazonaws.com:3306'
    db_user = 'admin'
    db_pass = '123456789'
    db_name = 'dbquiz'


    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(db_user, db_pass, db_host, db_name)

    SQLALCHEMY_POOL_RECYCLE = 500
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10

    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')

    # email server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'quizzery.quiz'
    MAIL_PASSWORD = '4esZXdr5@quizzery'

    # administrator list
    ADMINS = ['quizzery.quiz@gmail.com']