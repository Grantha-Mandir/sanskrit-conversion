from flask import Flask
from app.config import Config
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
import app.routes as routes