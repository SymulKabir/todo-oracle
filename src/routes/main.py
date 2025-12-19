from flask import Blueprint, jsonify, render_template;

home_route = Blueprint("home", __name__)
@home_route.route("/", methods=["GET"])
def home():
    return render_template("index.html")
    return "Hello from python app"