from flask import Flask, request, jsonify
from database import engine, db_session
from models import Base, Task


def create_app():
    app = Flask(__name__)
    Base.metadata.create_all(bind=engine)
    return app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/task", methods=['POST'])
def create_task():
    data = request.json
    if not data or data.get("name") is None:
        return jsonify({"message": "Please give `name` in json"}), 400
    new_task = Task(name=data["name"])
    db_session.add(new_task)
    db_session.commit()
    return jsonify({"result": new_task.as_dict()}), 201


@app.route("/task/<int:id>", methods=['PUT'])
def replace_task(id):
    data = request.json
    task = Task.query.filter(Task.id == id).first()
    if not task:
        return jsonify({"message": f"Task id {id} not found."}), 404
    if not data or data.get("id") is None or data.get("status") is None or data.get("name") is None:
        return jsonify({"message": f"Please give all fields(`id` `status` `id`) in json"}), 400
    task.status = True if data["status"] == 1 else False
    task.name = data["name"]
    db_session.commit()
    return jsonify({"result": task.as_dict()}), 200


@app.route("/task/<int:id>", methods=['DELETE'])
def remove_task(id):
    Task.query.filter(Task.id == id).delete()
    db_session.commit()
    return jsonify({"message": "success"}), 200


@app.route("/tasks", methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = {"result": []}
    for task in tasks:
        result["result"].append(task.as_dict())
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
