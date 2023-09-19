# This should hold our methods for inserting, modifying and deleting records in DB
from typing import Type
from backend.api.v1.models.data_models import Todos
from backend import db
from datetime import datetime

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

def create_todo(args: dict) -> tuple[bool, object]:
    task_id = args.get('task_id')
    task_name = args.get('task_name')
    task_details = args.get('task_details')
    task_status = args.get('task_status')
    task_deadline = datetime.strptime(args.get('task_deadline'), '%Y-%m-%d') #convert time w/ format YY-MM-DD to a datetime object
    
    new_todo = Todos(task_id=task_id, task_name=task_name, task_details=task_details,
                     task_status=task_status, task_deadline=task_deadline)
    
    try:
        db.session.add(new_todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {'message': f'{e}'}

    return True, {'message': 'Successfully added new todo'}