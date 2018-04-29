"""
Contains the Extensions to be used across application
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_oauthlib.provider import OAuth2Provider


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
oauth = OAuth2Provider()
