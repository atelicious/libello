# This is where the routes should be placed for our TODO api

# TODO: create a method where we add all api routes and return the api object once done
# This api object will be used on the main app.py as its resource 
from flask_restful import Api

# Add imports from controllers here
from controllers.todo_controller import Todo, TodoList

def create_resource(app):  
    #add the endpoints here from todo_handler
    api = Api(app)

    # add routes here
    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<todo_id>')

    return api
