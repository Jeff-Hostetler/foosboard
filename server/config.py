import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'foosball'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    ENVIRONMENT = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    ENVIRONMENT = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    ENVIRONMENT = 'test'
    TESTING = True