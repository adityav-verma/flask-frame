from sqlalchemy import create_engine
import pytest

from app.app import create_app
from app.extensions import db
from app.configs import TestConfig


@pytest.fixture(scope='session')
def app(request):
    """Session wide test `Flask` application"""
    app = create_app(TestConfig, 'TestApp')

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def setup_db(request, app):
    """Function wide fixture. Every testcase will have an isolated
    instance of the database
    """
    mysql_engine = create_engine(app.config.get('MYSQL_URI'))
    mysql_engine.execute(
        'CREATE DATABASE IF NOT EXISTS {}'.format(
            app.config.get('DB_NAME')
        )
    )
    db.create_all()
    def teardown():
        db.drop_all()

    request.addfinalizer(teardown)
    return db
