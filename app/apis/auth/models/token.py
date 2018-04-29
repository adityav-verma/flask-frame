from app.extensions import db
from app.utilities.models import BaseModel


class Token(db.Model, BaseModel):
    __tablename__ = 'tokens'
    client_id = db.Column(
        db.String(100), db.ForeignKey('clients.id'), nullable=False
    )
    client = db.relationship('Client')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')
    token_type = db.Column(db.String(50))
    access_token = db.Column(db.String(255), unique=True, nullable=False)
    refresh_token = db.Column(db.String(255), unique=True, nullable=False)
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []

    def delete(self):
        self.deleted = True
        return self.commit()
