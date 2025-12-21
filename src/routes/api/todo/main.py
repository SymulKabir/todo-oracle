from flask import Blueprint, jsonify, request, Blueprint;
from src.db.utility import execute_query;
import oracledb
from datetime import datetime

todo_route = Blueprint("todo_route", __name__);
TABLE_NAME = "TODO_ITEMS";

@todo_route.route("/", methods=["GET"])
def get_todo():
    sql = f"""
        SELECT id, title, description, status, created_at, due_date
        FROM {TABLE_NAME}
        ORDER BY id DESC
    """
    rows = execute_query(sql, fetch=True)

    todos = []
    for r in rows:
        todos.append({
            "id": r[0],
            "title": r[1],
            "description": r[2],
            "status": r[3],
            "created_at": r[4].strftime("%Y-%m-%d %H:%M:%S") if r[4] else None,
            "due_date": r[5].strftime("%Y-%m-%d %H:%M:%S") if r[5] else None
        })

    return jsonify({"data": todos})

@todo_route.route("/", methods=["POST"])
def create_todo():
    data = request.json

    title = data.get("title")
    description = data.get("description")
    status = data.get("status", "Pending")
    due_date = data.get("due_date")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    if due_date:
        sql = f"""
            INSERT INTO {TABLE_NAME} (title, description, status, due_date)
            VALUES (:title, :description, :status,
                    TO_TIMESTAMP(:due_date, 'YYYY-MM-DD HH24:MI:SS'))
        """
        params = {
            "title": title,
            "description": description,
            "status": status,
            "due_date": due_date
        }
    else:
        sql = f"""
            INSERT INTO {TABLE_NAME} (title, description, status, due_date)
            VALUES (:title, :description, :status, SYSTIMESTAMP)
        """
        params = {
            "title": title,
            "description": description,
            "status": status
        }

    execute_query(sql, params, commit=True)

    return jsonify({"message": "Todo created successfully"}), 201


@todo_route.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    sql = f"""
        DELETE FROM {TABLE_NAME}
        WHERE id = :id
    """

    params = {
        "id": id
    }

    execute_query(sql, params, commit=True)

    return jsonify({"message": "Todo deleted successfully", "success": True}), 200
