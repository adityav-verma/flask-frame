from flask import Blueprint

from app.extensions import oauth


auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/oauth/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return None
