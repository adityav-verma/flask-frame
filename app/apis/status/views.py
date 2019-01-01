from flask import Blueprint

from app.utilities import ApiResult

status = Blueprint('status', __name__, url_prefix='/api/status')


@todo.route('/', methods=['GET'])
def index():
    return ApiResult(
        payload={'status': 'OK'},
        message='Hello world'
    )
