# from flask import Flask
# from api.v1.resources.routes import create_resource
# from lib import routes
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from os.path import abspath, dirname, join
# from api.v1.resources.models.data_models import Todos
# from lib.constants import TaskStatus

# app = Flask(__name__)


# Goal: Postgresql DB configs
# put connections here for the postgres db
# Checkout Realpython guide here: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# For now, we will use SQLite to test the functionality of the API then migrate from there

# basedir = abspath(dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# api = create_resource(app)

# db.create_all()

# todo1 = Todos(task_id=1, task_name='Task 1', task_details='Sample Task 1', task_status=TaskStatus.NOT_YET_STARTED, 
#               created_at='', task_deadline='', stale_status=False)
# db.session.add(todo1)

# db.session.commit()

from backend import app

if __name__ == '__main__':
    app.run(debug=True)

## Scratch all of the models, stick to sqlite first then move towards postgres
## sample: https://www.codium.ai/blog/flask-sqlalchemy-tutorial/


# 9-18-2023: YAHOOOO abstraction is working for now