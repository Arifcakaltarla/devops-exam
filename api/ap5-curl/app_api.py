from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Study DevOps", "done": False},
    {"id": 2, "task": "Prepare AP5 curl", "done": True},
]

def next_id():
    return max(t["id"] for t in todos) + 1 if todos else 1

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"})

@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.get_json(silent=True) or {}
    task = data.get("task")
    if not task:
        return jsonify({"error": "task is required"}), 400

    item = {"id": next_id(), "task": task, "done": False}
    todos.append(item)
    return jsonify(item), 201

@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json(silent=True) or {}
    for t in todos:
        if t["id"] == todo_id:
            if "task" in data:
                t["task"] = data["task"]
            if "done" in data:
                t["done"] = bool(data["done"])
            return jsonify(t)
    return jsonify({"error": "not found"}), 404

@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    before = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]
    if len(todos) == before:
        return jsonify({"error": "not found"}), 404
    return jsonify({"deleted": todo_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
