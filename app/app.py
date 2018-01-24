from flask import Flask
from .configs import DefaultConfig

# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    if not app_name:
        app_name = DefaultConfig.APP_NAME

    app = Flask(app_name)

    configure_app(app, config)
    configure_blueprints(app)

    return app


def configure_app(app, config=None):
    """
    Load config to the app and add additional configurations if needed
    http://flask.pocoo.org/docs/0.12/api/#configuration
    """
    # Laod the default config
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from .api import api
    from .auth import auth
    for bp in [api, auth]:
        app.register_blueprint(bp)
