from backend import db
from lib.constants import TaskStatus
from sqlalchemy import func
from datetime import datetime


class Todos(db.Model):
    __tablename___ = 'todos_table'

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(100), nullable=False, unique=True)
    task_details = db.Column(db.String(300), nullable=False)
    task_status = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    task_deadline = db.Column(db.DateTime(), nullable=True)
    stale_status = db.Column(db.Boolean, default=False)

    # def __init__(self, task_id: int, task_name: str, task_details: str, task_status: TaskStatus,
    #              task_deadline: str, stale_status: bool = False, created_at : str = datetime.now()):
    #     self.task_id = task_id
    #     self.task_name = task_name
    #     self.task_details = task_details
    #     self.task_status = task_status
    #     self.created_at = created_at
    #     self.task_deadline = task_deadline
    #     self.stale_status = stale_status

    def __repr__(self):
        return f'<Todo object {self.task_id} - {self.task_name} >'
    
    def to_dict(self):
        return {
            'task_id' : self.task_id,
            'task_name' : self.task_name,
            'task_details' : self.task_details,
            'task_status' : self.task_status,
            'created_at' : str(self.created_at),
            'task_deadline' : str(self.task_deadline),
            'stale_status' : self.stale_status,
        }