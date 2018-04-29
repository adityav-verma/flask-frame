from flask import Blueprint, request

from app.utilities import ApiResult
from app.utilities.schema_validators import validate_request_schema
from app.todo.schemas import NewTodoSchema
from app.todo.models.todo import Todo


todo = Blueprint('todo', __name__, url_prefix='/todo')


@todo.route('/', methods=['GET'])
def index():
    return ApiResult(
        payload={},
        message='Hello from Python.. hzzzzz..'
    )


@todo.route('/', methods=['POST'])
@validate_request_schema(schema=NewTodoSchema)
def new():
    data = request.json
    todo = Todo.add(data['title'], data['content'])
    return ApiResult(
        payload=todo.to_dict(),
        message='Todo created!',
        status=201
    )
