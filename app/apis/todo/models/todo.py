from app.extensions import db
from app.utilities.models import BaseModel


class Todo(db.Model, BaseModel):
    __tablename__ = 'todos'
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='todos', uselist=False)

    def __str__(self):
        return ('Id: {}, Title: {}'.format(self.id, self.title))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

    @classmethod
    def add(cls, title, content, user):
        """Add a Todo for a user
        Args:
            - title: str
            - content: str
            - user: User obj
        Returns:
            - Todo obj
        """
        todo = cls(title=title, content=content, user=user)
        return todo.commit()
