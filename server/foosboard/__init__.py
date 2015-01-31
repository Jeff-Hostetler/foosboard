import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

if os.environ.get('FLASK_ENV', None) == 'test':
    app_settings = 'config.TestConfig'
else:
    app_settings = 'config.DevelopmentConfig'

app = Flask(__name__)
app.config.from_object(app_settings)
CORS(app, resources=r'/api/*', allow_headers='Content-Type')

db = SQLAlchemy(app)

import endpoints
