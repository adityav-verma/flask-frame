from datetime import datetime

from app.extensions import db


class BaseModel:
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=False
    )
    deleted_at = db.Column(db.DateTime, nullable=True)

    def commit(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as E:
            db.session.rollback()
            raise E

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as E:
            db.session.rollback()
            raise E
