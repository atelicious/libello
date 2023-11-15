# This should hold our methods for inserting, modifying and deleting records in DB
from typing import Type
from app.models.todos import Todos
from app import db
from datetime import datetime
from typing import List


def get_all_todo() -> List:
    """
    Returns all TODO items on DB as a List
    """
    return Todos.query.all()


def get_todo_by_id(todo_id: int) -> tuple[bool, Todos]:
    """
    Gets todo using todo_id, returns True and the todo object when founds
    """

    if not todo_id and type(todo_id) != int:
        return False, {"message": "No todo_id provided"}

    try:
        todo = Todos.query.get(todo_id)
    except Exception as e:
        return False, {"message": f"{e}"}

    if not todo:
        return False, {"message": f"No todo with todo_id : {todo_id}"}

    return True, todo


def update_todo_by_id(todo: Todos, args: dict) -> tuple[bool, dict]:
    # Get all updated details from the POST body

    # Prevent updating of the todo object if the body contains protected fields
    protected_fields = ["id", "created_at", "stale_status"]
    protected_field_check = any(fields in args.keys() for fields in protected_fields)

    if protected_field_check:
        return False, {"message": "Cannot update protected fields"}

    for keys, values in args.items():
        if hasattr(todo, keys):
            setattr(todo, keys, values)
        else:
            return False, {
                "message": f'Error updating todo attribute "{keys}" with value "{values}"'
            }

    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {"message": f"{e}"}

    return True, None


def create_todo(args: dict) -> tuple[bool, dict]:
    # task_id = args.get("task_id")
    task_name = args.get("task_name")
    task_details = args.get("task_details")
    task_status = args.get("task_status")
    task_deadline = args.get("task_deadline")
    if task_deadline:
        task_deadline = datetime.strptime(
            task_deadline, "%Y-%m-%d"
        )  # convert time w/ format YY-MM-DD to a datetime object

    new_todo = Todos(
        # task_id=task_id,
        task_name=task_name,
        task_details=task_details,
        task_status=task_status,
        task_deadline=task_deadline,
    )

    try:
        db.session.add(new_todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {"message": f"{e}"}

    return True, None


def delete_todo_by_id(todo_id: int) -> tuple[bool, dict]:
    success, todo = get_todo_by_id(todo_id)
    if not success:
        return False, {"message": "Cannot delete non-existing todo"}

    try:
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False, {"message": f"{e}"}

    return True, None
