from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World'})
