from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import mail

app = Flask(__name__)
app.config.from_object()
app.config.from_object('config.Config')

db = SQLAlchemy(app)
mail.init_app(app)

from . import views, models, tasks
