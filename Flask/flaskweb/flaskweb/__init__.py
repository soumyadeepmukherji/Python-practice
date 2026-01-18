from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Configiration
app.config['SECRET_KEY'] = 'cb379004254134eeaac465f53f38def8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Inisialization of Instance
db = SQLAlchemy(app) # For Database

bcrypt = Bcrypt(app) # For Hasing Of Password

login_manager = LoginManager(app) # For login system

from flaskweb import routes # Import Routes