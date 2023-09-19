# This should hold our methods for inserting, modifying and deleting records in DB
from typing import Type
from backend.api.v1.models.data_models import Todos

def get_todo_by_id(todo_id: int) -> tuple[bool, object]:
    """Gets todo using todo_id, returns a tuple and the todo object when found
    """
    
    if not todo_id and type(todo_id) != int:
        return False, {'message': 'No todo_id provided'}
    
    try:
        todo = Todos.query.get(todo_id)
    except Exception as e:
        return False, {'message': f'{e}'}

    if not todo:
        return False, {'message': f'No todo with todo_id : {todo_id}'}

    return True, todo

def update_todo_by_id(todo_id: int) -> tuple[bool, dict]:
    pass

