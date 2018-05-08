from flask import Blueprint, request

from app.utilities import ApiResult
from app.extensions import oauth
from app.utilities.schema_validators import validate_request_schema

from .schemas import NewTodoSchema
from .models.todo import Todo


todo = Blueprint('todo', __name__, url_prefix='/api/todo')


@todo.route('/', methods=['GET'])
@oauth.require_oauth('email')
def index():
    user = request.oauth.user
    return ApiResult(
        payload={'todos': [todo.to_dict() for todo in user.todos]},
        message='Listing all todos'
    )


@todo.route('/', methods=['POST'])
@oauth.require_oauth('email')
@validate_request_schema(schema=NewTodoSchema)
def new():
    data = request.json
    todo = Todo.add(data['title'], data['content'], request.oauth.user)
    return ApiResult(
        payload=todo.to_dict(),
        message='Todo created!',
        status=201
    )
