from flask import Blueprint, jsonify

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World'})
