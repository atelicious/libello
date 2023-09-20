# This should hold our methods for inserting, modifying and deleting records in DB
from typing import Type
from backend.api.v1.models.data_models import Todos
from backend import db
from datetime import datetime
from ast import literal_eval

def get_todo_by_id(todo_id: int) -> tuple[bool, Todos]:
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

def update_todo_by_id(todo: Todos, args: dict) -> tuple[bool, dict]:
    updated_details = literal_eval(args.get('updated_task_details'))
    protected_fields = ['id', 'created_at', 'stale_status']

    #prevent updating of id, created_at, and stale_status for now
    protected_field_check = any(fields in updated_details.keys() for fields in protected_fields)

    if protected_field_check:
        return False, {'message': f'Cannot update protected fields'}
    
    for keys, values in updated_details.items():
        if hasattr(todo, keys):
            setattr(todo, keys, values)
        else: 
            return False, {'message': f'Error updating todo attribute "{keys}" with value "{values}"'}

    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {'message': f'{e}'}
    
    return True, {'message: successfully edited todo'}

def create_todo(args: dict) -> tuple[bool, dict]:
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

def delete_todo_by_id(todo_id: int) -> tuple[bool, dict]:

    success, todo = get_todo_by_id(todo_id)
    if not success:
        return False, {'message': 'Cannot delete non-existing todo'}
    
    try:
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {'message': f'{e}'}
    
    return True, {'message': 'successfully deleted todo record'}