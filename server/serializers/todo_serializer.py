from app import ma
from models.todoModel import Todo

from marshmallow import fields

class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True