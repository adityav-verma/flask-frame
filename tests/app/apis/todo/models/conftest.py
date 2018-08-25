import pytest

from tests.factories.user_factory import UserFactory


@pytest.fixture
def test_add_1():
    title = 'Test title'
    content = 'Test content'
    user = UserFactory.create()
    return {
        'params': {
            'user': user,
            'title': title,
            'content': content
        },
        'title': title,
        'content': content,
        'user': user
    }
