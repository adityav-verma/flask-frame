from app.extensions import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text())

    def __str__(self):
        return ('Id: {}, Title: {}'.format(self.id, self.title))

    def _commit(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def add(cls, title, content):
        todo = cls(title=title, content=content)
        return todo._commit()
