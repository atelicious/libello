from flask_restful import Api
from backend.api.v1.controllers.todo_controller import TodoList, Todo

# Add imports from controllers here

def create_resource(app): 
    #add the endpoints here from todo_handler
    api = Api(app)

    # add routes here
    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<todo_id>')

    return api