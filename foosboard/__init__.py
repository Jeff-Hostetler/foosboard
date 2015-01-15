import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True
    SECRET_KEY = 'foosball'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)

import games.views
