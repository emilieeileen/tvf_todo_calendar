from app import db
from models.base import BaseModel


class Todo(db.Model, BaseModel):
    __tablename__ = 'todo'
    name = db.Column(db.String(50), nullable=False, unique=True)
    date = db.Column(db.String(50), nullable=False, unique=True)
    
    