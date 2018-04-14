from .configs import DefaultConfig
from .extensions import db, migrate
from .api_flask import ApiFlask
from .exceptions import ApiException


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    if not app_name:
        app_name = DefaultConfig.APP_NAME

    app = ApiFlask(app_name)

    configure_app(app, config)
    configure_blueprints(app)
    configure_db(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    """Load config to the app and add additional configurations if needed
    http://flask.pocoo.org/docs/0.12/api/#configuration
    """
    # Load the default config
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def configure_db(app):
    """Configure SQLAlchemy"""
    db.init_app(app)
    migrate.init_app(app, db)


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from .todo import todo
    from .auth import auth
    for bp in [todo, auth]:
        app.register_blueprint(bp)


def configure_error_handlers(app):
    """Configure automatic exception handling"""
    app.register_error_handler(ApiException, lambda err: err.to_result())
