from app.todos import bp
from flask import jsonify, request
from app.lib.db_methods import (
    get_todo_by_id,
    get_all_todo,
    create_todo,
    update_todo_by_id,
    delete_todo_by_id,
)
from app.schema.todo_schema import (
    AddNewTodoSchema,
    ModifyTaskDeadlineSchema,
    ModifyTodoSchema,
)
from app.lib.utils import missing_required_params
from datetime import datetime

@bp.route("/", methods=["GET", "POST"], strict_slashes=False)
def index():
    if request.method == "GET":
        todos = get_all_todo()
        return jsonify([todo.to_dict() for todo in todos]), 200

    if request.method == "POST":
        data = request.json
        missing_params, message = missing_required_params(AddNewTodoSchema, data)

        if missing_params:
            return jsonify(message), 400

        success, message = create_todo(data)

        if not success:
            return jsonify(message), 400

        return jsonify({"status": "Successfully added new TODO item"}), 201


@bp.route("/<int:todo_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def process_todo(todo_id: int):
    """Handles per-todo crud operations

    GET - render page for the specific todo
    PUT - edit todo details
    DELETE - delete specific todo
    """

    if request.method == "GET":
        success, content = get_todo_by_id(todo_id)

        if not success:
            return jsonify(content), 404

        return jsonify(content.to_dict()), 200

    if request.method == "PUT":
        modified_data = request.json

        missing_params, message = missing_required_params(
            ModifyTodoSchema, modified_data
        )

        if missing_params:
            return jsonify(message), 400

        success, content = get_todo_by_id(todo_id)
        if not success:
            return jsonify(content), 404

        success, message = update_todo_by_id(content, modified_data)

        if not success:
            return jsonify(message), 400

        return jsonify({"status": "Successfully edited todo details"}), 200

    if request.method == "DELETE":

        success, message = delete_todo_by_id(todo_id)

        if not success:
            return jsonify(message), 400
        
        return jsonify({"status": "Successfully deleted TODO item"}), 200


@bp.route("/<int:todo_id>/task_deadline", methods=["PUT"], strict_slashes=False)
def update_task_deadline(todo_id: int):
    if request.method == "PUT":
        data = request.json

        missing_params, message = missing_required_params(
            ModifyTaskDeadlineSchema, data
        )

        if missing_params:
            return jsonify(message), 400

        data["task_deadline"] = datetime.strptime(data["task_deadline"], "%Y-%m-%d")

        success, content = get_todo_by_id(todo_id)
        if not success:
            return jsonify(content), 404

        success, message = update_todo_by_id(content, data)

        if not success:
            return jsonify(message), 400

        return jsonify({"status": "Successfully edited todo details"}), 200
