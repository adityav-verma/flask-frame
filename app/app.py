from flask import Flask

# For import *
__all__ = ['create_app']


def create_app():
    """Create an app instance based on the passed params"""
    app = Flask(__name__)
    configure_blueprints(app)
    return app


def configure_blueprints(app):
    """Register all blueprints with the app"""
    # TODO: Figure out why . is needed
    from .api import api
    for bp in [api]:
        app.register_blueprint(bp)
