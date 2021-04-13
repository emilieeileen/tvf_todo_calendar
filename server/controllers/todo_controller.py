from flask import Blueprint, request
from models.todoModel import Todo
from serializers.todo_serializer import TodoSchema
todo_schema = TodoSchema()
from marshmallow.exceptions import ValidationError


router = Blueprint(__name__, "todos")

@router.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    print(todos)
    return todo_schema.jsonify(todos, many=True), 200


@router.route("/todos", methods=["POST"])
def create_todo():
    todo_dictionary = request.json
    try:
        todo = todo_schema.load(todo_dictionary)
    except ValidationError as e:
        return { 'errors': e.messages, 'messages': 'Something went wrong'}
    todo.save()
    return todo_schema.jsonify(todo), 200


@router.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    existing_todo = Todo.query.get(todo_id)
    todo_dictionary = request.json
    try:
        todo = todo_schema.load(
            todo_dictionary,
            instance=existing_todo,
            partial=True
        )
    except ValidationError as e:
        return { 'errors': e.message, 'messages': 'Something went wrong'}
    todo.save()
    
    return todo_schema.jsonify(todo), 200

@router.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)

    todo.remove()

    return { 'message': 'So sad, todo has been deleted' }, 200
