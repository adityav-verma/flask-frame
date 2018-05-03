from flask import current_app
from werkzeug.security import gen_salt

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

    def to_dict(self):
        """Return a dictionary representation of the User object"""
        return {
            'username': self.username,
            'email': self.email
        }

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
        salt = gen_salt(50)
        user = cls(
            username=username, password=cls._generate_password(password, salt),
            email=email, salt=salt
        )
        return user.commit()
