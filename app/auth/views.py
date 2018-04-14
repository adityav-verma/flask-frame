from flask import Blueprint, jsonify
from app.utilities import ApiResult

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/', methods=['GET'])
def index():
    return ApiResult(
        payload={},
        message='Auth APIs'
    )
