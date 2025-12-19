from flask import Blueprint, jsonify, Blueprint;
from src.routes.api.todo.main import todo_route


api_route = Blueprint("api_route", __name__);
api_route.register_blueprint(todo_route, url_prefix="/todo")

@api_route.route("/", methods=["GET"])
def get_users(): 
    return "hello from api route"
