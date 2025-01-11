from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from environment import Settings

# Create the Flask application instance.
app = Flask(__name__, template_folder='../templates')
app.config.from_object(Settings)

# Create other facilities for the application.
db = SQLAlchemy(app)
jwt = JWTManager()
bcrypt = Bcrypt(app)
