from flask import current_app
from base64 import b64encode
from os import urandom


from app.extensions import db, bcrypt
from app.utilities.models import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(100), nullable=False)

    def _check_password(self, candidate):
        """
        Validate a candidate password with actual password
        """
        candidate_salt = candidate + self.salt
        return bcrypt.check_password_hash(self.password, candidate_salt)

    @classmethod
    def _generate_salt(cls, len=20):
        """
        Generate a salt to be used along with password to improve security
        """
        random_bytes = urandom(len)
        return b64encode(random_bytes).decode('utf-8')

    @classmethod
    def _generate_password(cls, password, salt):
        """
        Hash password using bcrypt. A standard defined.
        """
        password_salt = password + salt
        return bcrypt.generate_password_hash(
            password_salt, rounds=current_app.config.get('BCRYPT_ROUNDS')
        )

    @classmethod
    def add(cls, username, password, email):
        """Create a user"""
        salt = cls._generate_salt()
        user = cls(
            username=username, password=cls._generate_password(password, salt),
            email=email, salt=salt
        )
        return user.commit()
