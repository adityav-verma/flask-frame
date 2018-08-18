import factory

from app.extensions import db
from app.apis.auth.models.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'
    username = 'test'
    email = 'test@test.com'
    password = 'pass'
    salt = 'salt'
