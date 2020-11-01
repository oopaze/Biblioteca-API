import os
from datetime import timedelta

class Config(object):
    JWT_AUTH_USERNAME_KEY = 'username'
    JWT_EXPIRATION_DELTA = timedelta(days=30)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_AUTH_URL_RULE = '/login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    basedir = os.path.abspath(os.path.dirname(__file__))


class Development(Config):
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'biblioteca.db')
    if "DATABASE_URI" in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI'] 


class Production(Config):
    ENV = 'production'
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'biblioteca.db')
    if "DATABASE_URI" in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']     

    
