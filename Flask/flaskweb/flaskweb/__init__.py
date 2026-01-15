from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configiration
app.config['SECRET_KEY'] = 'cb379004254134eeaac465f53f38def8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskweb import routes