from app.extensions import db
from app.utilities.models import BaseModel


class Todo(db.Model, BaseModel):
    __tablename__ = 'todos'
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text())

    def __str__(self):
        return ('Id: {}, Title: {}'.format(self.id, self.title))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

    @classmethod
    def add(cls, title, content):
        todo = cls(title=title, content=content)
        return todo.commit()
