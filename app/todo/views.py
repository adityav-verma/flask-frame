from flask import Blueprint, jsonify
import json

from app.utilities import ApiResult
from app.todo.models.todo import Todo

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['GET'])
def index():
    return ApiResult(
        payload={},
        message='Hello from Python.. hzzzzz..'
    )


@todo.route('/', methods=['POST'])
def new():
    todo = Todo.add('Yo!', 'Jessi Pinkman')
    return ApiResult(
        payload=todo.to_dict(),
        message='Todo created!',
        status=201
    )
