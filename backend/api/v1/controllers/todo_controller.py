from flask_restful import Resource
from backend.api.v1.models.data_models import Todos
from lib.db_methods import get_todo_by_id, update_todo_by_id, create_todo, delete_todo_by_id
from lib.todo_parser import todo_parser, update_todo_parser

# TODO: This is working for now, but move forward with blueprints in the future

class Todo(Resource):
    """Handles the getting, modifying & deleting of TODOS via GET, PUT & DELETE
    
    GET: Get a single TODO using todo_id
    PUT: Modify a TODO using todo_id
    DELETE: Delete a TODO using todo_id
    """
    
    def get(self, todo_id):
        success, content = get_todo_by_id(todo_id)

        if not success:
            #TODO: add logging here
            return content, 404
        
        return content.to_dict(), 200
    
    def put(self, todo_id):
        parser = update_todo_parser()
        args = parser.parse_args()
        args = dict((key, value) for key, value in args.items() if value)

        success, todo_obj = get_todo_by_id(todo_id)

        if not success:
            #TODO: add logging here
            return content, 404
        
        success, content = update_todo_by_id(todo_obj, args)

        if not success:
            return content, 400

        return f'Successfully updated TODO with id: {todo_id}', 201
    
    def delete(self, todo_id):
        success, content = delete_todo_by_id(todo_id)

        if not success:
            return content, 404

        return content, 200

class TodoList(Resource):
    """Handles the obtaining all TODOS and adding of TODOS via GET & POST
    
    GET: Get all TODOS in DB
    POST: Add a new TODO record in DB
    """

    def get(self):
        todos = Todos.query.all()
        print(todos)

        return ('DB is missing', 500) if todos is None else [todo.to_dict() for todo in todos]

    def post(self):
        parser = todo_parser()
        args = parser.parse_args()

        # Map all keys and values of the POST request body into a dictionary if the value existss
        args = dict((key, value) for key, value in args.items() if value)
        success, content = create_todo(args)

        if not success:
            return content, 400
        
        return content, 201