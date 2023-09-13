from app import db
from sqlalchemy.sql import func

# Place our Postgres Models here

"""
What should an item look like in DB

{task_id:'Task ID', task_name:'Task Name', 'task_details':'Task details', 'task_status':'Task status', 'created_at':'Date when task is created', 
'task_deadline':'Tasks defined deadline', 'stale_status': 'True/False'}

Sample Model (SQLAlchemy)

db = SQLAlchemy(app)

class TodoModel(db.Model)
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_details = db.Column(db.String(300), nullable=False)
    task_status = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    task_deadline = db.Column(db.DateTime(), nullable=False)
    stale_status = db.Column(db.Boolean, server_default=False, default=False)

    def __repr__(self):
        return f'<Todo object {self.task_id} - {self.task_name} >'
"""


class Todos(db.Model):
    __tablename___ = 'todos_table'

    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_details = db.Column(db.String(300), nullable=False)
    task_status = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    task_deadline = db.Column(db.DateTime(), nullable=False)
    stale_status = db.Column(db.Boolean, server_default=False, default=False)

    def __init__(self, task_id, task_name, task_details, task_status, created_at,
                 task_deadline, stale_status):
        self.task_id = task_id
        self.task_name = task_name
        self.task_details = task_details
        self.task_status = task_status
        self.created_at = created_at
        self.task_deadline = task_deadline
        self.stale_status = stale_status

    def __repr__(self):
        return f'<Todo object {self.task_id} - {self.task_name} >'
