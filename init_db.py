# initialize db script here
from app import app, db
from app.lib.constants import TaskStatus
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    from app.models.todos import Todos

    todo1 = Todos(
        task_id=1,
        task_name="Task 1",
        task_details="Sample task 1 details",
        task_status=TaskStatus.NOT_YET_STARTED.value,
        task_deadline=datetime(2023, 9, 20),
    )

    db.session.add(todo1)

    todo2 = Todos(
        task_id=2,
        task_name="Task 2",
        task_details="Sample task 2 details",
        task_status=TaskStatus.ONGOING.value,
        task_deadline=datetime(2023, 9, 20),
    )

    db.session.add(todo2)
    db.session.commit()

    db.session.close()

print("Successfully initialized DB")
