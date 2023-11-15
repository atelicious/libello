# This holds all of our parsers for TODO requests
from __future__ import annotations
from flask_restful import reqparse


def todo_parser() -> reqparse.RequestParser:
    parser = reqparse.RequestParser()
    parser.add_argument("task_name", required=True)
    parser.add_argument("task_details", required=True)
    parser.add_argument("task_status", required=True)
    parser.add_argument("task_deadline", required=True)

    return parser


def update_todo_parser() -> reqparse.RequestParser:
    parser = reqparse.RequestParser()
    parser.add_argument("updated_task_details", required=True)

    return parser
