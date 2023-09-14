# Temporary name, this will hold all classes regarding TODO retrieval and modification

from flask_restful import reqparse, Resource
from api.v1.resources.models.data_models import Todos

# Sample TODO DB, will be changed to a standard Postgres DB once APIs are done
DB = {
    'todo1': {'task': 'Task details'},
    'todd2': {'task': 'Task details'},
    'todo3': {'task': 'Task details'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

def get_todo_by_id(todo_id):

    if not todo_id in DB:
        return False, {'status':'todo_id not in DB'}

    return True, DB[todo_id]

# TODO
# this will be the new TODO resource, refactor this more

class Todo(Resource):

    # Get specific todo by todo_id
    def get(self, todo_id):

        success, content = get_todo_by_id(todo_id)

        if not success:
            #TODO: add logging here
            return content, 404
        
        return content, 200
    
    # Update specific todo by todo_id

    def put(self, todo_id):

        success, content = get_todo_by_id(todo_id)

        if not success:
            # TODO: add logging here
            return content, 404
        
        args = parser.parse_args()
        new_task = {'task': args['task']}
        
        # Set new task in DB
        # TODO: add logging here
        DB[todo_id] = new_task

        return f'Successfully updated TODO with id: {todo_id}', 201

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

        return ('DB is missing', 500) if todos is None else todos

    # Add new todo item
    def post(self):

        args = parser.parse_args()
        # get current max todo_id on DB, and add 1
        todo_id = int(max(DB.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        
        # TODO: add logging here and handling if we can't connect to DB
        DB[todo_id] = {'task': args['task']}

        return f'Successfully added TODO {todo_id}', 201