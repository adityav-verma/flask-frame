from flask import Blueprint, jsonify
from app.todo.models.todo import Todo

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World'})

@todo.route('/', methods=['POST'])
def new():
    todo = Todo.add('Yo!', 'Jessi Pinkman')
    return jsonify({'Title': todo.title})
