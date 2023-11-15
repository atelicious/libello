# Put Todos Model here

from app.extensions import db
from sqlalchemy import func


class Todos(db.Model):
    """DB Model for the TODO object

    Attributes:
    task_id : int, autoincrement, task id of todo
    task_name : unique, task name of todo
    task_details : text, task details of todo
    task_status : str, TaskStatus Enum, task status todo
    created_at : datetime, time when todo is created
    task_deadline : datetime, task deadline set
    stale_status : bool, stale status of the todo
    last_modified: datetime, records when todo is last modified
    """

    __tablename___ = "todos_table"

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(100), nullable=False, unique=True)
    task_details = db.Column(db.String(300), nullable=False)
    task_status = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    task_deadline = db.Column(db.DateTime(), nullable=True)
    stale_status = db.Column(db.Boolean, default=False)
    last_modified = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return f"<Todo object {self.task_id} - {self.task_name} >"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_name": self.task_name,
            "task_details": self.task_details,
            "task_status": self.task_status,
            "created_at": str(self.created_at),
            "task_deadline": str(self.task_deadline),
            "stale_status": self.stale_status,
            "last_modified": str(self.last_modified),
        }
