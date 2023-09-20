# Temporary name, this will hold all classes regarding TODO retrieval and modification

from flask_restful import reqparse, Resource
from backend.api.v1.models.data_models import Todos
from lib.db_methods import get_todo_by_id, update_todo_by_id, create_todo
from flask import request
from sqlalchemy import func
from lib.todo_parser import todo_parser, update_todo_parser


# Sample TODO DB, will be changed to a standard Postgres DB once APIs are done
DB = {
    'todo1': {'task': 'Task details'},
    'todd2': {'task': 'Task details'},
    'todo3': {'task': 'Task details'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

# def get_todo_by_id(todo_id):

#     if not todo_id in DB:
#         return False, {'status':'todo_id not in DB'}

#     return True, DB[todo_id]

# TODO
# this will be the new TODO resource, refactor this more

class Todo(Resource):

    # Get specific todo by todo_id
    def get(self, todo_id):

        success, content = get_todo_by_id(todo_id)

        if not success:
            #TODO: add logging here
            return content, 404
        
        return content.to_dict(), 200
    
    # Update specific todo by todo_id

    def put(self, todo_id):

        # success, content = get_todo_by_id(todo_id)

        # if not success:
        #     # TODO: add logging here
        #     return content, 404
        
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
        
        # TODO: add logging here
        # success, content = update_todo_by_id(content)

        return f'Successfully updated TODO with id: {todo_id}', 201
        # return content, 201
# TODO
# this will handle showing all todos, and adding new tods via POST

class TodoList(Resource):

    # Get all todos on DB

    def get(self):

        # TODO: remember that we need to have a postgres method here for 
        # querying all DB entries
        # In the future we need to query todos based on other categories so
        # need to refactor this as well

        todos = Todos.query.all()
        print(todos)

        return ('DB is missing', 500) if todos is None else [todo.to_dict() for todo in todos]

    # Add new todo item
    def post(self):

        parser = todo_parser()
        args = parser.parse_args()

        # Map all keys and values of the POST request body into a dictionary if the value existss
        args = dict((key, value) for key, value in args.items() if value)
        success, content = create_todo(args)

        if not success:
            return content, 400

        # TODO: add logging here and handling if we can't connect to DB
        # DB[todo_id] = {'task': args['task']}
        return content, 201