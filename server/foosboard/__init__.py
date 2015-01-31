import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
CORS(app, resources=r'/api/*', allow_headers='Content-Type')

db = SQLAlchemy(app)

import endpoints
