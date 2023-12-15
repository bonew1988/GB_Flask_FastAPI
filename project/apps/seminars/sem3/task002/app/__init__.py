from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap  # Импортируйте Bootstrap

app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../library.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)  # Инициализируйте Bootstrap

from app import routes
