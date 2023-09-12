from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from lib import routes

app = Flask(__name__)
api = routes.create_resource(app)

if __name__ == '__main__':
    app.run(debug=True)


    
    

