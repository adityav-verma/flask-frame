from app.extensions import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text())
