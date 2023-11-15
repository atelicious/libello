from flask import Flask

from config import Config
from app.extensions import db  # DB is declared in extensions

app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB
db.init_app(app)

# Import blueprints here
from app.main import bp as main_bp
from app.todos import bp as todos_bp

# Add blueprints to app
app.register_blueprint(main_bp)
app.register_blueprint(todos_bp, url_prefix="/todos")
