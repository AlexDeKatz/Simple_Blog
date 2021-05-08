from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__, template_folder='./views')
# app.config['SECRET_KEY'] = "4ca9bfbc52dcf3ef11c6fd4902196d05"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config.from_pyfile('../environment.cfg')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)