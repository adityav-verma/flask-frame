from .configs import DefaultConfig
from .api_flask import ApiFlask
from .exceptions import ApiException
from .utilities import ApiResult


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    if not app_name:
        app_name = DefaultConfig.APP_NAME

    app = ApiFlask(app_name)

    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
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


def configure_extensions(app):
    """Configure SQLAlchemy"""
    from .extensions import db, migrate, bcrypt, oauth
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    oauth.init_app(app)


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from .apis.todo import todo
    from .apis.auth import auth
    from .apis.status import status
    for bp in [todo, auth, status]:
        app.register_blueprint(bp)


def configure_error_handlers(app):
    """Configure automatic exception handling"""
    app.register_error_handler(ApiException, lambda err: err.to_result())
    app.register_error_handler(
        Exception, lambda err: ApiResult({}, str(err), 500)
    )
    # Jsonschema error handlers start block
    from jsonschema.exceptions import ValidationError, SchemaError
    app.register_error_handler(
        ValidationError, lambda err: ApiResult({}, str(err), 400)
    )
    app.register_error_handler(
        SchemaError, lambda err: ApiResult({}, str(err), 400)
    )
    # Jsonschema error handlers end block
