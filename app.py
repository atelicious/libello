from flask import Flask
from lib import routes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = routes.create_resource(app)

# Postgresql DB configs
# put connections here for the postgres db
# Checkout Realpython guide here: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

if __name__ == '__main__':
    app.run(debug=True)
