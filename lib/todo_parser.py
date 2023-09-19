# This holds all of our parsers for TODO requests
from flask_restful import reqparse


def todo_parser() -> object:
    parser = reqparse.RequestParser()
    parser.add_argument('task_name', required=True)
    parser.add_argument('task_details', required=True)
    parser.add_argument('task_status', required=True)
    parser.add_argument('task_deadline', required=True)

    return parser
    