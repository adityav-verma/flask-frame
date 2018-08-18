import pytest


@pytest.mark.usefixtures('setup_db')
class TestAdd:
    def test_1(self):
        assert 1 == 1
