from flask import Flask, request, make_response
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="barax",
    description="REST API for our guild management application.",
)


@app.route("/users")
def index():
    all_users = {"users": users}
    return all_users


@app.route("/users", methods=["POST"])
def create():
    user = {
        "name": request.json["name"],
        "email": request.json["email"],
        "password": request.json["password"],
    }
    users.append(user)
    return make_response("", 204)


@app.route("/users/<int:user_id>", methods=["DELETE"])
def destory(user_id):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            del users[i]
            break
    return make_response("", 204)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            users[i]["name"] = request.json.get("name")
            users[i]["email"] = request.json.get("email")
            users[i]["password"] = request.json.get("password")
    return make_response("", 204)


users = [
    {
        "id": 1,
        "name": "Zuggernaut",
        "email": "3stanbrooks@gmail.com",
        "password": "password",
    },
    {
        "id": 2,
        "name": "Toothfully",
        "email": "emavro19@gmail.com",
        "password": "password",
    },
]
