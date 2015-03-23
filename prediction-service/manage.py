import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from foosboard import app, db

if os.getenv('FLASK_ENV', 'development') == 'test':
    app_settings = 'config.TestConfig'
else:
    app_settings = 'config.DevelopmentConfig'

app.config.from_object(app_settings)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
