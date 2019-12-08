from flask import Flask
from app.config import Config
app = Flask(__name__)
app.config.from_object(Config)

import app.routes as routes