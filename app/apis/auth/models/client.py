from werkzeug.security import gen_salt

from app.extensions import db
from app.utilities.models import BaseModel
import uuid


class Client(db.Model, BaseModel):
    __tablename__ = 'clients'
    name = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer(), autoincrement=True)
    client_id = db.Column(db.String(100), default=uuid.uuid4, primary_key=True)
    secret = db.Column(db.String(50), nullable=False, index=True, unique=True)
    _is_confidential = db.Column(db.Boolean, default=True, nullable=False)
    _allowed_grant_types = db.Column(db.Text, nullable=False)
    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split(' ')
        return []

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split(' ')
        return []

    @property
    def client_type(self):
        return 'confidential' if self._is_confidential else 'public'

    @property
    def default_redirect_uri(self):
        if self.redirect_uris:
            return self.redirect_uris[0]
        else:
            return None

    @property
    def allowed_grant_types(self):
        if self._allowed_grant_types:
            return self._allowed_grant_types.split(' ')
        return []

    @classmethod
    def generate_test_client(cls):
        item = Client(
            secret=gen_salt(50),
            _default_scopes='email',
            _is_confidential=True,
            _allowed_grant_types='password',
            name="LoginClient",
        )
        db.session.add(item)
        db.session.commit()
        return item
