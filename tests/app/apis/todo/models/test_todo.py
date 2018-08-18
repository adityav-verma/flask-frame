import pytest

from app.apis.todo.models.todo import Todo


@pytest.mark.usefixtures('setup_db')
class TestAdd:
    def test_1(self, test_add_1):
        data = test_add_1
        new_todo = Todo.add(**data['params'])
        assert new_todo is not None
        assert new_todo.id is not None
        assert new_todo.title == data['title']
        assert new_todo.content == data['content']
        assert new_todo.user == data['user']
