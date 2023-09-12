from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from lib import routes

app = Flask(__name__)
api = routes.create_resource(app)

# TODOS = {
#     'todo1': {'task': 'Task 1'},
#     'todo2': {'task': 'Task 2'},
#     'todo3': {'task': 'Task 3'},
# }

# def existing_todo(todo_id):
#     if todo_id in TODOS:
#         return True
#     return False
    
# parser = reqparse.RequestParser()
# parser.add_argument('task')


# TODO
# shows a single todo item and lets you update & delete a task

# class Todo(Resource):

#     # Get specific todo by todo_id
#     def get(self, todo_id):

#         if not existing_todo(todo_id):
#             return f"TODO ID {todo_id} does not exist in DB", 404
        
#         return TODOS[todo_id]

#     def put(self, todo_id):

#         if not existing_todo(todo_id):
#             return f"TODO ID {todo_id} does not exist in DB", 404

#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
        
#         return f'Succesfully updated {task}', 201
    
#     def delete(self, todo_id):

#         if not existing_todo(todo_id):
#             return f"TODO ID {todo_id} does not exist in DB", 404
        
#         del TODOS[todo_id]

#         return f"Successfully deleted TODO with TODO_ID = {todo_id}", 200
    

# TODOList
# shows a list of all todos, and lets you add new todos via POST

# class TodoList(Resource):

#     def get(self):

#         return ('DB is missing', 500) if TODOS is None else TODOS
    
#     def post(self):

#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}

#         return f"Succesfully added TODO {TODOS[todo_id]}", 201

## Setup API resource routing

# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


    
    

