from app.models.todos import Todos

# from app import ma
from marshmallow import Schema, fields, validate


class AddNewTodoSchema(Schema):
    task_name = fields.Str(validate=validate.Length(min=5), required=True)
    task_details = fields.Str(required=True)
    task_status = fields.Str(required=True)
    task_deadline = fields.Date()


class ModifyTaskDeadlineSchema(Schema):
    task_deadline = fields.Date(required=True)


class ModifyTodoSchema(Schema):
    task_name = fields.Str(validate=validate.Length(min=5))
    task_details = fields.Str()
    task_status = fields.Str()
