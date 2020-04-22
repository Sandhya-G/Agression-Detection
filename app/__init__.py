from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
#to let flask know which view function handles login
login.login_view = 'login'
#imported at the bottom and not at the top of the script to avoid circular imports
from app import routes,models